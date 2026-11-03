import flet as ft
import backend

def main(page: ft.Page):
  page.title = "Japanese B Vocabulary Quiz"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.window.width = 450
  page.window.height = 650
  page.window.resizable = False
    
  quiz_type_dropdown = ft.Dropdown(
    label="Select Question Type",
    options=[
      ft.dropdown.Option(key="1", text="Kanji -> Meaning"),
      ft.dropdown.Option(key="2", text="Kanji -> Reading"),
      ft.dropdown.Option(key="3", text="Reading -> Meaning"),
      ft.dropdown.Option(key="4", text="Meaning -> Reading"),
    ],
    width=350,
  )

  num_questions_slider = ft.Slider(
    min=1,
    max=50,
    divisions=49,
    value=10,
  )
    
  num_questions_text = ft.Text("Number of Questions: 10", weight=ft.FontWeight.BOLD)

  def slider_changed(e):
    num_questions_text.value = f"Number of Questions: {int(e.control.value)}"
    page.update()

  num_questions_slider.on_change = slider_changed

  category_dropdown = ft.Dropdown(
    label="Select Category",
    options=[
      ft.dropdown.Option(key="1", text=backend.categories[1]["name"]),
      ft.dropdown.Option(key="2", text=backend.categories[2]["name"]),
      ft.dropdown.Option(key="3", text=backend.categories[3]["name"]),
      ft.dropdown.Option(key="4", text=backend.categories[4]["name"]),
      ft.dropdown.Option(key="5", text=backend.categories[5]["name"]),
      ft.dropdown.Option(key="6", text=backend.categories[6]["name"]),
      ft.dropdown.Option(key="7", text=backend.categories[7]["name"]),
    ],
    width=350,
  )

  error_text = ft.Text("", color=ft.Colors.ERROR)

  def start_button_clicked(e):
    if not quiz_type_dropdown.value or not category_dropdown.value:
      error_text.value = "Please select both a question type and a category."
      page.update()
      return
    
    num_questions = int(num_questions_slider.value)
    quiz_type = backend.quiz_configs[int(quiz_type_dropdown.value)]
    category = backend.categories[int(category_dropdown.value)]

    start_quiz(page, quiz_type, num_questions, category)

  start_button = ft.Button(
    "Start Quiz",
    icon=ft.Icons.PLAY_ARROW_ROUNDED,
    on_click=start_button_clicked,
    width=350,
    height=45,
  )

  page.add(
    ft.Container(
      content=ft.Column(
        [
          ft.Text("Japanese B Vocabulary Quiz", size=22, weight=ft.FontWeight.BOLD),
          ft.Divider(),
          quiz_type_dropdown,
          ft.Container(height=10),
          num_questions_text,
          num_questions_slider,
          ft.Container(height=5),
          category_dropdown,
          error_text,
          ft.Container(height=10),
          start_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      padding=20,
    )
  )

def start_quiz(page: ft.Page, quiz_type, num_questions, category):
  page.session.store.set("score", 0)
  working_questions, working_answers = backend.get_working_list(quiz_type, category)
  show_question(page, working_questions, working_answers, quiz_type, 1, num_questions)

def show_question(page: ft.Page, working_questions, working_answers, quiz_type, num, num_questions):
  page.clean()
  page.bottom_appbar = None

  score = page.session.store.get("score")

  def again_button_clicked():
    page.clean()
    main(page)

  def exit_button_clicked():
    quit()

  again_button = ft.Button(
    "Play again",
    icon=ft.Icons.PLAY_ARROW_ROUNDED,
    on_click=again_button_clicked,
    width=150,
    height=45,
  )

  exit_button = ft.Button(
    "Exit",
    icon=ft.Icons.EXIT_TO_APP,
    on_click=exit_button_clicked,
    width=150,
    height=45,
  )

  if num > num_questions:
    page.add(
      ft.Container(
            content=ft.Column(
              [
                ft.Text("Quiz finished!", size=30, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                ft.Text(f"Your score is: {score}/{num_questions}", size=30, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                ft.Row(
                  [
                    again_button,
                    ft.Container(width=10),
                    exit_button
                  ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
              ],
              alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
          )
      )
    page.update()
    return

  question = backend.get_question(working_questions)
  response = ft.TextField("", hint_text=f"Type the correct {quiz_type["target_key"]}: ")
  error_text = ft.Text("", color=ft.Colors.ERROR)

  def submit_button_clicked(e):
    if not response.value:
      error_text.value = "Please type your response."
      page.update()
      return
    else:
      if backend.check_answer(response.value, question, working_answers, quiz_type):
        page.session.store.set("score", score + 1)
        answer_box.content = ft.Text("Correct!", size=22, weight=ft.FontWeight.BOLD)
        answer_box.bgcolor = ft.Colors.GREEN_500
      else:
        answer_box.content = ft.Text(f"Inorrect!, {working_answers[question]}", size=22, weight=ft.FontWeight.BOLD)
        answer_box.bgcolor = ft.Colors.RED_500
      button.content = proceed_button

  def proceed_button_clicked(e):
    show_question(page, working_questions, working_answers, quiz_type, num + 1, num_questions)

  submit_button = ft.Button(
    "Submit resposne",
    icon=ft.Icons.PLAY_ARROW_ROUNDED,
    on_click=submit_button_clicked,
    width=350,
    height=45,
  )

  proceed_button = ft.Button(
    "Proceed",
    icon=ft.Icons.PLAY_ARROW_ROUNDED,
    on_click=proceed_button_clicked,
    width=350,
    height=45,
  )

  button = ft.Container(content=submit_button)

  answer_box = ft.Container(
    content=ft.Text(""),
    bgcolor=None,
    padding=15,
    alignment=ft.Alignment.CENTER,
    width=350,
    height=60,
    )

  page.bottom_appbar = answer_box
  
  page.add(
    ft.Container(
      content=ft.Column(
        [
          ft.Text(f"Question {num}/{num_questions}", size=22, weight=ft.FontWeight.BOLD),
          ft.Container(height=50),
          ft.Text(working_questions[question], size=30, weight=ft.FontWeight.BOLD),
          ft.Container(height=10),
          response,
          ft.Container(height=10),
          button,
          error_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      padding=20,
    )
  )

if __name__ == "__main__":
  ft.run(main)