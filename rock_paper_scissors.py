
# To be submittted with GitHub :(
# Rename to main.py

import random

print("Hola! Let's play a Rock-Paper-Scissors game, shall we?")

user_options = ["R", "P", "S"]
cpu_options = ["Rock", "Paper", "Scissors"]

while True:
    print("NOTE: To select an option, enter: \n> 'R' for 'Rock', \n> 'P' for 'Paper', \n> 'S' for 'Scissors'.")
    choice = input("\n> ")

    if choice.upper() not in user_options and choice.upper() != 'Q':
        print("Error! '{}' is invalid. Try again or enter 'Q' to quit.".format(choice))
        if choice.upper() == 'Q':
            print("Okay, you quit.")
            break
    else:
        break

cpu_choice = random.choice(cpu_options)

u_choice = choice.split()

if choice.upper() == "R":
    u_choice.append("ock")
elif choice.upper() == "P":
    u_choice.append("aper")
elif choice.upper() == "S":
    u_choice.append("cissors")

user_choice = ("").join(u_choice).title()

print("\nPlayer ({}) : CPU ({})".format(user_choice, cpu_choice))

while True:
    if user_choice == cpu_choice:
        print("\nIt's a tie. Restarting game...\n")
        
        while True:
            print("NOTE: To select an option, enter: \n> 'R' for 'Rock', \n> 'P' for 'Paper', \n> 'S' for 'Scissors'.")
            choice = input("\n> ")

            if choice.upper() not in user_options and choice.upper() != 'Q':
                print("Error! '{}' is invalid. Try again or enter 'Q' to quit.".format(choice))
                if choice.upper() == 'Q':
                    print("Okay, you quit.")
                    break
            else:
                break

        cpu_choice = random.choice(cpu_options)

        u_choice = choice.split()

        if choice.upper() == "R":
            u_choice.append("ock")
        elif choice.upper() == "P":
            u_choice.append("aper")
        elif choice.upper() == "S":
            u_choice.append("cissors")

        user_choice = ("").join(u_choice).title()

        print("\nPlayer ({}) : CPU ({})".format(user_choice, cpu_choice))
    else:
        break

if user_choice == "Rock" and cpu_choice == "Paper":
    print("Uh-oh! Paper covers Rock, Computer wins!")
elif user_choice == "Paper" and cpu_choice == "Rock":
    print("Yay! Paper covers Rock, You win!")
elif user_choice == "Rock" and cpu_choice == "Scissors":
    print("Yay! Rock blunts Scissors, You win!")
elif user_choice == "Scissors" and cpu_choice == "Rock":
    print("Uh-oh! Rock blunts Scissors, Computer wins!")
elif user_choice == "Paper" and cpu_choice == "Scissors":
    print("Uh-oh! Scissors cuts Paper, Computer wins!")
elif user_choice == "Scissors" and cpu_choice == "Paper":
    print("Yay! Scissors cuts Paper, You win!")
else:
    print("Something went wrong, try again.")
