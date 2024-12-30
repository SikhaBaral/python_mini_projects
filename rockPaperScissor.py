import random


choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("Select Rock, Paper, or Scissors? ").lower()

if player == computer:
    print("computer = ", computer)
    print("player ", player)
    print("TIE")

elif player == "paper":
    if computer == "rock":
        print("computer = ", computer)
        print("player = ", player)
        print("You Lose")
    if computer == "scissor":
        print("computer = ", computer)
        print("player = ", player)
        print("You WIN")
elif player == "rock":
    if computer == "paper":
        print("computer = ", computer)
        print("player = ", player)
        print("You WIN")
    if computer == "scissor":
        print("computer = ", computer)
        print("player = ", player)
        print("You Lose")
elif player == "scissor":
    if computer == "paper":
        print("computer = ", computer)
        print("player = ", player)
        print("You WIN")
    if computer == "rock":
        print("computer = ", computer)
        print("player = ", player)
        print("You Lose")


