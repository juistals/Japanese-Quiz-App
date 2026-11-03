import random
import re
import json
from pathlib import Path

question_file = Path(__file__).parent / "vocabulary_data.json"

with question_file.open("r", encoding="utf-8") as f:
    vocabulary_data = json.load(f)

quiz_configs = {
    1: {"prompt_key": "kanji", "target_key": "meaning", "category": None},
    2: {"prompt_key": "kanji", "target_key": "reading", "category": None},
    3: {"prompt_key": "reading", "target_key": "meaning", "category": None},
    4: {"prompt_key": "meaning", "target_key": "reading", "category": None},
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

def get_question(working_questions):
    question = random.randint(0, len(working_questions) - 1)
    return question    

def get_working_list(quiz_type, category):
    p_key, t_key = quiz_type["prompt_key"], quiz_type["target_key"]
    start, end = category["starting_index"], category["ending_index"]
    words = vocabulary_data[start:end+1]
    if "reading" in (p_key, t_key):
        words = [w for w in words if w["reading"] != 'x']
    working_questions = [w[p_key] for w in words]
    working_answers = [w[t_key] for w in words]
    return working_questions, working_answers

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