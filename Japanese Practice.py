import random
import re
import json
from pathlib import Path

question_file = Path(__file__).parent / "Vocabulary Data.json"

with question_file.open("r", encoding="utf-8") as f:
    vocabulary_data = json.load(f)

quiz_configs = {
    1: {"prompt_key": "kanji", "target_key": "meaning", "category": None},
    2: {"prompt_key": "kanji", "target_key": "reading", "category": None},
    3: {"prompt_key": "reading", "target_key": "meaning", "category": None},
    4: {"prompt_key": "meaning", "target_key": "reading", "category": None},
    5: {"prompt_key": "reading", "target_key": "kanji", "category": None}
}

categories = {
    1: {"name": "General Exam Terms", "starting_index": 0, "ending_index": 87},
    2: {"name": "Identities", "starting_index": 456, "ending_index": 611},
    3: {"name": "Experiences", "starting_index": 612, "ending_index": 676},
    4: {"name": "Human Ingenuity", "starting_index": 220, "ending_index": 337},
    5: {"name": "Social Organization", "starting_index": 338, "ending_index": 465},
    6: {"name": "Sharing the Planet", "starting_index": 88, "ending_index": 219},
    7: {"name": "All categories", "starting_index": 0, "ending_index": 676}
}

def choose_quiz():
    print("There are 4 question types:")
    print("1. kanji -> meaning")
    print("2. kanji -> reading")
    print("3. reading -> meaning")
    print("4. meaning -> reading")

    while True:
        user_input = input("Choose the question type (1-4): ") 
        if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
             print("Please choose a valid type")
             continue
        else: break

    quiz_type = quiz_configs[int(user_input)]

    while True:
        user_input = input("Choose the number of question (1 - 50): ")
        try: 
            num_questions = int(user_input)
            if num_questions <= 0 or num_questions > 50:
                print("Please choose a number between 1 and 50.")
                continue
        except ValueError:
            print("Please choose a valid number")
        else: break

    print("There are 7 categories")
    print("1. General Exam Terms")
    print("2. Identities")
    print("3. Experiences")
    print("4. Human Ingenuity")
    print("5. Social Organization")
    print("6. Sharing the Planet")
    print("7. All categories")

    while True:
            user_input = input("Choose the category (1-7): ") 
            if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5" and user_input != "6" and user_input != "7":
                 print("Please choose a valid type")
                 continue
            else: break

    category = categories[int(user_input)]

    return quiz_type, num_questions, category

def start_quiz(num_questions, working_questions, working_answers, quiz_type):
    score = 0

    for i in range(num_questions):
        question = get_question(working_questions)
        print(working_questions[question])
        response = get_response(quiz_type)
        if check_answer(response, question, working_answers, quiz_type):
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print(f"The answer is {working_answers[question]}")
    return score

def get_question(working_questions):
    question = random.randint(0, len(working_questions) - 1)
    return question    

def get_working_list(quiz_type, category):
    p_key, t_key = quiz_type["prompt_key"], quiz_type["target_key"]
    start, end = category["starting_index"], category["ending_index"]
    words = vocabulary_data[start:end]
    if "reading" in (p_key, t_key):
        words = [w for w in words if w["reading"] != 'x']
    working_questions = [w[p_key] for w in words]
    working_answers = [w[t_key] for w in words]
    return working_questions, working_answers

def get_response(quiz_type):
    return input(f"Type the correct {quiz_type["target_key"]}: ") 

def check_answer(response, question, working_answers, quiz_type):
    if quiz_type["target_key"] == "meaning":
        answer = get_answer_list(working_answers[question])
        response = clean_text(response)
        if response in answer:
            return True
    else:
        if response == working_answers[question]:
            return True
    return False

def handle_game_over(score):
    print(f"Your score is: {score}")
    print("Type: 'again' to do one more quiz or 'exit' to exit")

    while True:
        option = input("Choose an option: ")
        if option != "again" and option != "exit":
            print("Please choose a valid option")
        else:
            break
    
    if option == "again":
        main()
    elif option == "exit":
        quit()

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"^(the|a|an)\s+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def get_answer_list(answer):
    answer_list = []
    for i in range(len(answer)):
        if "(" in answer[i]:
            full = answer[i].replace("(", "").replace(")", "")
            answer_list.append(clean_text(full))
            no_brackets = re.sub(r"\(.*?\)", "", answer[i])
            answer_list.append(clean_text(no_brackets))
        else:
            answer_list.append(clean_text(answer[i]))
    return answer_list

def main():
    print("This is a vocabulary and kanji quiz to prepare for the IB Japanese B exams!")
    quiz_type, num_questions, category = choose_quiz()
    working_questions, working_answers = get_working_list(quiz_type, category)
    score = start_quiz(num_questions, working_questions, working_answers, quiz_type)
    handle_game_over(score)

if __name__ == "__main__":
    main()