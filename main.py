from question_bank import load_questions
from user_manager import UserManager
from quiz_engine import QuizEngine

def main():
    """Provides Interactive CLI and Module Orchestration[cite: 1]."""
    user_mgr = UserManager()
    questions = load_questions()
    quiz = QuizEngine(questions)

    print("==============================================")
    print("   Welcome to Python Algorithmic Quiz System  ")
    print("==============================================")

    while True:
        print("\n1. Register\n2. Login & Take Quiz\n3. View Profile & Analytics\n4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            success, msg = user_mgr.register_user(uname, pwd)
            print(msg)
            
        elif choice == "2":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            if user_mgr.authenticate_user(uname, pwd):
                print(f"\nWelcome, {uname}!")
                # The quiz asks 10 random questions out of the 50 provided
                score = quiz.run_quiz(num_questions=10)
                total_asked = min(10, len(questions))
                user_mgr.record_score(uname, score, total_asked)
                print(f"\nQuiz Finished! You scored: {score}/{total_asked}")
            else:
                print(" Invalid credentials!")
                
        elif choice == "3":
            uname = input("Enter username: ")
            history = user_mgr.get_user_history(uname)
            if history:
                max_s, avg_s = quiz.calculate_analytics(history)
                print(f"\n--- History for {uname} ---")
                for idx, record in enumerate(history, 1):
                    print(f"Attempt {idx}: Score {record[0]}/{record[1]} ({record[2]:.1f}%)")
                print(f"Highest Score: {max_s} | Average Score: {avg_s:.2f}")
            else:
                print("No history found or invalid user.")
                
        elif choice == "4":
            print("Thank you for using the Quiz App!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
