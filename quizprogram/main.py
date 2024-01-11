quiz = {
    "quiz 1": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
   "quiz 2": {
        "question": "What is the capital of Qatar?",
        "answer": "Doha"
    },
    "quiz 3": {
        "question": "What is the capital of Taiwan?",
        "answer": "Taipei"
    },
    "quiz 4": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "quiz 5": {
        "question": "What is the capital of Zimbabwe?",
        "answer": "Harare"
    },
    "quiz 6": {
        "question": "Who will be the president of Indonesia in 2024?",
        "answer": "Udin"
    }
}

score = 0

for key, value in quiz.items():
    print(key)
    print(value["question"])
    answer = input("Your answer: ")
    
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print("Your score is", score, "\n")
    else:
        print("Wrong!!!")
        print("The answer is", value["answer"])
        print("Your score is", score, "\n")
    
    while key == "quiz 6":
        if answer.lower() == value["answer"].lower():
            print("Correct")
            score += 1
            print("Your score is", score, "\n")
            quiz_completed = True
            break
        else:
            print("Try again !!!")
            print(key)
            print(value["question"])
            answer = input("Your answer: ")
        
    

print("You got " + str(score) + " out of 6 questions correctly")
print("Your percentage is " + str(int(score/6 * 100)) + "%")
print("Program ended")

        



