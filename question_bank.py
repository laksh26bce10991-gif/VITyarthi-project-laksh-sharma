import json
import os

# Automatically pinpoint the folder where the script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def is_prime(n: int) -> bool:
    """Factoring Algorithm: Checks if a number is prime (Unit 4)."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def load_questions():
    """Returns the list of quiz questions by loading the external JSON file."""
    question_file = os.path.join(BASE_DIR, "questions.json")
    try:
        with open(question_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"\n[ERROR] Could not find 'questions.json'.\nMake sure it is saved in: {BASE_DIR}")
        return []
    except json.JSONDecodeError:
        print("\n[ERROR] Invalid JSON syntax in 'questions.json'. Please check syntax.")
        return []