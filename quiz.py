# quiz.py
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "answer": "C"
    }
]

def start_quiz():
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    start_quiz()
