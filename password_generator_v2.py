import string
import random
print("Welcome to the Password Generator! ")

password = ""

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

num_letters = int(input("How many letters would you like to use?:\n"))
num_numbers = int(input("How many numbers would you like to use?:\n"))
num_symbols = int(input("How many symbols would you like to use?:\n"))

for characters in range(1, num_letters + 1):
    characters = random.choice(letters)
    password += characters

for characters in range(1, num_numbers + 1):
    characters = random.choice(numbers)
    password += characters

for characters in range(1, num_symbols + 1):
    characters = random.choice(symbols)
    password += characters

print(password)
