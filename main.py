import json
import os

def run_quiz(quiz):
    score = 0
    for text in quiz:
        print(text["question"])
        for key,value in text["options"].items():
            print(f"{key}) {value}")
        user_answer = input("Your answer is: ")
        if user_answer == text["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
    return score
    
def read_quiz_from_json(filename):
    data = []
    with open(filename) as f:
        data = json.load(f)
    return data    

def save_results_to_json(filename, quiz_result):
    quiz_results = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                quiz_results = json.load(f) or []
            except json.decoder.JSONDecodeError:
                pass
    quiz_results.append(quiz_result)
    with open(filename, "w") as f:
        json.dump(quiz_results, f, indent=2)


quiz = read_quiz_from_json("quiz.json")
score = run_quiz(quiz)
first_name = input("Enter your name: ")
save_results_to_json("results.json", {"first_name": first_name, "score": score})
print(f"Your score is: {score}")
