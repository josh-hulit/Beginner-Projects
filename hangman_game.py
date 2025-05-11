#   Hangman Game
import random

# hangman art:
stages = [r'''

        +---+
        |   |
        0   |
       /|\  |     
       / \  |
            |
            |
      ======|
          
    ''', r'''
          
        +---+
        |   |
        0   |
       /|   |    
       / \  |
            |
            |
      ======|

    ''', r'''
        +---+
        |   |
        0   |
        |   |    
       / \  |
            |
            |
      ======|

    ''', r'''
        +---+
        |   |
        0   |
        |   |    
         \  |
            |
            |
      ======|

    ''', r'''
        +---+
        |   |
        0   |
        |   |    
            |
            |
            |
      ======|

      ''', r'''
        +---+
        |   |
        0   |
            |    
            |
            |
            |
      ======|

      ''', r'''
        +---+
        |   |
            |
            |    
            |
            |
            |
      ======|

''']

word_list = ["axiom", "absurd", "avenue", "buffalo", "blizzard", "boxcar", "cobweb", "dynamite", '\n'
             "dwarves", "embezzle", "espionage", "fishhook", "jaundice", "jukebox", "keyhole", "larynx", '\n'
             "microwave", "mystify", "nightclub", "oxidize", "pajama", "polka", "psyche", "tractor", '\n'
             "unknown", "vaporize", "voodoo", "whiskey", "xylophone", "youthful", "zephyr"]

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
print(f"You have {lives} guesses remaining")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, wrong letter. You have {lives} guesses remaining.")
        if lives == 0:
            game_over = True
            print("YOU LOSE.")
            print(f"The answer is {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("YOU WIN!!!")

    print(stages[lives])
