# Define a dictionary with trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "How many continents are there?": "7",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which year did the Titanic sink?": "1912"
}

# Display and check answers using a for loop
for question, correct_answer in trivia_questions.items():
    # Display the question to the user
    print(question)

    # Prompt the user to input their answer
    user_answer = input("Your answer: ")

    # Check if the user's answer matches the correct answer
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.\n")

# End of the trivia questions
print("You've completed the trivia questions. Great job!")
