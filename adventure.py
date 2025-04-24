print("Welcome to the Choose your Adventure Game!")

name = input("What is your name: ")

print("Hello " + name + "!")

play_game = input("Would you like to play? (yes/no): ").lower()

if play_game == "yes" or play_game == "y":
    print("Thanks for playing, let's get started!")

    direction = input(
        "Which direction would you like to go? (left/right): ").lower()
    if direction == "left":
        print("You have come to a dead end. Game over")
    elif direction == "right":
        print("This path has led you to a bridge.")
        print(
            "You cannot see the other side of the bridge,\nbut the water underneath is dark.")
        print("You can try to cross over the bridge, or attempt to go under,\nthrough the water.")
        over_under = input(
            "Would you like to cross over the bridge or under,\nthrough the water? (over/under): ").lower()
        if over_under == "over":
            print("As you cross over, the bridge collapses and you die. Game Over.")
        elif over_under == "under":
            print("You were eaten by an alligator. Game Over.")


else:
    print("I'm sorry, please come back later. ")
