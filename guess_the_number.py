
# Number Guessing Game

import random

lowest_number = 1
highest_number = 1000

answer = random.randint(lowest_number, highest_number)

guesses = 0
is_running = True

print("Welcome to the Number Guessing Game")
print(f"Please select a number between {lowest_number}\
       and {highest_number}: ")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

    else:
        print("Invalid Response")
        print(f"Please select a number between {lowest_number}\
                  and {highest_number}: ")

    if guess < lowest_number or guess > highest_number:
        print("Number out of range")
        print(f"Please select a number between {lowest_number}\
               and {highest_number}: ")

    elif guess < answer:
        print("Too low, please try again: ")

    elif guess > answer:
        print("Too high, please try again: ")

    else:
        print("CONGRATULATIONS !!!!!")
        print(f"You got the answer in {guesses} tries!")
        print("End")
        is_running = False
