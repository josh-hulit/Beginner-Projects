# Rock Paper Scissors Game
import random

options = ("rock", "paper", "scissors")

player_choice = None
computer_choice = random.choice(options)

while player_choice not in options:
    player_choice = input("Rock, Paper, or Scissors: ").lower()

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

if computer_choice == player_choice:
    print("It's a draw")
elif computer_choice == "rock" and player_choice == "paper":
    print("You Win")
elif computer_choice == "scissors" and player_choice == "rock":
    print("You Win")
elif computer_choice == "paper" and player_choice == "scissors":
    print("You Win")
else:
    print("You Lose")

print("Thanks for playing.")
