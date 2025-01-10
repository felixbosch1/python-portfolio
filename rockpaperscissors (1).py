#Felix Bosch
#1/6/2025
#Rock Paper Scissors
#Initiate
import random
#Functions
wins = 0
def won():
    global wins
    wins = wins + 1
losses = 0
def lost():
    global losses
    losses = losses + 1
ties = 0
def tie():
    global ties
    ties = ties + 1
def game():
    print("Welcome to Rock, Paper, Scissors")
while True:
    print("Please select one of the three options")
    player = input("Selection: ")
    player = player.lower()
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    elif computer == 3:
        computer = "scissors"

    if player == computer:
        print("Tie")
        tie()
    elif player == "rock" and computer == "scissors":
        print("You win")
        won()
    elif player == "rock" and computer == "paper":
        print("You lose")
        lost()
    elif player == "paper" and computer == "rock":
        print("You win")
        won()
    elif player == "paper" and computer == "scissors":
        print("You lose")
        lost()
    elif player == "scissors" and computer == "rock":
        print("You lose")
        lost()
    elif player == "scissors" and computer == "paper":
        print("You win")
        won()
    else:
        print("Wrong input")

    print("Your record: ")
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))


    again = input("Would you like to play again (yes or no): ")
    again = again.lower()
    if again == "yes":
        print("Good luck")
    elif again == "no":
        print("Thanks for playing")
        break

#main
game()


