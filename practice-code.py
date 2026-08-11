import random

game_pick = ["rock", "paper", "scissor"]

while True:
    print("\n\n-----------------------------------")
    print("Let's play a game!")
    menu = input("\n[1] Start\n[2] Quit\n\nPress 1 to start & press 2 to quit\n\nChoose: ")

    if menu == "1":
        print("\n-----------------------------------")
        print("This game called 'Rock, Paper, Scissor'.\nThe game is simple:\nType if you want to choose 'rock'\nType if you want to choose 'paper'\nType if you want to choose 'scissor'\n\nWin againts CPU to break the loop, Goodluck!\n\n")

        while True:
            print("\n\n-----------------------------------")
            user = input("Your choice: ")
            cpu = random.choice(game_pick)
    
            if user == cpu:
                print("\n\n-----------------------------------")
                print("It's a tie, try again!")
                continue
            elif ((user == "rock" and cpu == "scissors")
                or (user == "scissors" and cpu == "rock")
                or (user == "paper" and cpu == "rock")
                ):
                print("\n\n-----------------------------------")
                print("You won!")
                break
            elif user not in game_pick:
                print("Invalid input, try again!")
                continue
            else:
                print("\n\n-----------------------------------")
                print("You Lose!")
                continue

    elif menu == "2":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, try again!")
        continue
    
