import random
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player 1, make your move: ").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")


if player == computer:
    print("It's a tie !")
elif player == "rock":
    if computer == "scissors":
        print("player win !")
    elif computer == "paper":
        print("Computer wins !")
elif player == "paper":
    if computer == "rock":
        print("player wins !")
    elif computer == "scissors":
        print("Computer wins !")
elif player == "scissors":
    if computer == "paper":
        print("player wins !")
    elif computer == "rock":
        print("Computer wins !")
else:
    print("somthing went wrong")