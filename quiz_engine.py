import random
from utils import find_maximum

class QuizEngine:
    """Controls execution flow, evaluates input, and calculates statistics[cite: 1]."""
    def __init__(self, questions):
        self.questions = questions

    def run_quiz(self, num_questions=10) -> int:
        """Executes the quiz using loops and conditionals (Unit 3)[cite: 1]."""
        if not self.questions:
            print("\nNo questions available. Please check 'questions.json'.")
            return 0

        score = 0
        total_to_ask = min(num_questions, len(self.questions))
        selected_questions = random.sample(self.questions, total_to_ask)

        print(f"\n--- Starting Quiz ({total_to_ask} Random Questions) ---")
        
        for i, q in enumerate(selected_questions):
            print(f"\nQ{i+1}: {q['question']}")
            for idx, opt in enumerate(q["options"], 1):
                print(f"  {idx}. {opt}")

            while True:
                try:
                    user_choice = input("Select option number: ").strip()
                    if user_choice.isdigit() and 1 <= int(user_choice) <= len(q["options"]):
                        choice_int = int(user_choice)
                        break
                    print(f"Please enter a number between 1 and {len(q['options'])}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if choice_int == q["answer"]:
                print(" Correct!")
                score += 1
            else:
                print(f" Incorrect! Correct answer was option: {q['answer']}")
                
        return score

    def calculate_analytics(self, scores_list):
        """Calculates highest score using fundamental max algorithm[cite: 1]."""
        if not scores_list:
            return 0, 0
        raw_scores = [s[0] for s in scores_list]
        max_score = find_maximum(raw_scores)
        avg_score = sum(raw_scores) / len(raw_scores)
        return max_score, avg_score