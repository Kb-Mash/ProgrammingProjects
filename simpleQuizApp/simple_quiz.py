# Simple Quiz App
# A basic Python console application that presents multiple-choice questions


'''
def main():
    print("Welcome to the Simple Quiz App!")
    print("Please answer the following questions:")

    score = 0

    # Question 1
    answer1 = input("What is the capital of France? ")
    if answer1.lower() == "paris":
        score += 1

    # Question 2
    answer2 = input("What is 2 + 2? ")
    if answer2 == "4":
        score += 1

    # Question 3
    answer3 = input("Who wrote 'To Kill a Mockingbird'? ")
    if answer3.lower() == "harper lee":
        score += 1

    print(f"Your final score is: {score}/3")

if __name__ == "__main__":
    main()
'''


def run_quiz():
    # Define the quiz questions as a list of dictionaries
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": 1  # Index of correct answer (0-based)
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": 1
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": 1
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "answer": 1
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Welcome to the Simple Quiz!\n")
    
    # Loop through each question
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        
        # Get user input
        while True:
            try:
                user_answer = int(input("\nYour answer: ")) - 1  # Convert to 0-based index
                if 0 <= user_answer < len(q['options']):
                    break
                else:
                    print("Please enter a number between 1 and", len(q['options']))
            except ValueError:
                print("Please enter a valid number.")
        
        # Check answer
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q['options'][q['answer']]
            print(f"Incorrect! The correct answer is {correct_option}.\n")
    
    # Display final results
    percentage = (score / total_questions) * 100
    print("Quiz Complete!")
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")
    
    # Provide feedback based on score
    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")



if __name__ == "__main__":
    run_quiz()