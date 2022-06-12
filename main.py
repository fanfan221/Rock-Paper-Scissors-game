#import random module
import random

#print a welcome message and give the rules of the game.
print('''
=====================================
Welcome to Rock-Paper-Scissors game!

Possible options:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors"

Game rules:
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
=====================================
''')

# create a list of possible options.
list_of_choices = ["R", "P", "S"]

# This dictionary will helps us decide of a winner. The keys win to their corresponding value according to the game rules.
wins_to = {"R":"S", "P":"R", "S":"P"}

# Main game loop.
while True: 
    # player input loop
    while True:
        # ask player to pick an option
        player_choice = input('Pick an option between R, P or S\n')

        #Make the program case in sensentive for R, S, and P.
        player_choice = player_choice.upper()

        # Check if the user input is valid
        if player_choice not in list_of_choices:
            print("Invalid choice!") # if the input is invalid the program will keep asking for an input
        
        # if input is valid, exit player input loop
        else:
            break

    # make a choice for CPU           
    CPU_choice = random.choice(list_of_choices)
   
    # display both player and CPU moves.
    print(f"Player({player_choice}) : CPU({CPU_choice})")

    # Print the winner if there one
    if player_choice == wins_to[CPU_choice]: # CPU wins 
        print("CPU wins!")
        break

    if CPU_choice == wins_to[player_choice]: # player wins
        print("Player wins!")
        break

    # there is a tie!
    print('''It's a tie!
Please play again.
    ''')


    
        




