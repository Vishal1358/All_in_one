def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in option[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

def check_answer(answer,guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses,guesses):
    print("RESULTS")

    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses:",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
def play_again():
    response = input("Do you want to play again? (yes or no):")
    response = response.upper()

    if response == "YES":
        return True
    return False

questions = {
    "Who created Python?:":"A",
    "What year was python created?":"B",
    "Python is tributed to which comedy group?:":"C",
    "Is the Eart round:":"A",
    "Which type of Programming does Python support?" : "D",
    "What is the print statement in Python": "A"
}

option = [["A. Guido Van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True","B. False", "C. sometimes", "D. What's Earth?"],
    ["A. Object-oriented programming","B. Structured programming","C. Functional programming","D. All of the mentioned"],
    ["A. print()","B. P()", "C. echo()", "D. pr()"]
]

new_game()

while play_again():
    new_game()

print("Byeeeee!")