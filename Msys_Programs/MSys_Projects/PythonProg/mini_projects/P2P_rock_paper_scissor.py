print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")


if player1 == "rock" and player2 == "scissors":
    print("player1 wins !")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins !")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins !")
elif player1 == "paper" and player2 == "scissor":
    print("player2 wins !")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins !")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins !")

elif player == player2:
    print("It's a tie !")
else:
    print("somthing went wrong")