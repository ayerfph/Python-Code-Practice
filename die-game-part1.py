# Import package needed
import random

# Creating roll a die code
die = ["1", "2", "3", "4", "5", "6"]

while True:
    
    # Player input
    print("\n\nGuess the number a die show!\n")
    p = input("Choose from 1 to 6: ")
    
    # A die roll:
    d = random.choice(die)

    # If player input wrong number:
    if p not in die:
        print("\n\nYou put wrong input, Choose again!")
        continue

    # Show the player's guess and die number show after roll:
    print("\n\nYour guess: ", p)
    print("Number in die: ", d)

    # Condition if the player guessed the number right:
    if p == d:
        print("\n\nYou guessed right!")
        break
    else:
        print("\n\nYou guessed wrong, try again folks!")
        continue
