#project 4 : Rock, paper & scissor game.

import random

#game choices
choices = ["rock" , "paper" , "scissors"]

#player choices
player_choice = input("enter rock , paper , or scissors: ").lower()

#computer choice
computer_choice = random.choice(choices)

#winner decision
if player_choice == computer_choice:
    print(f"dono ka choice {player_choice} tha. its a tie!")
elif player_choice == "rock" and computer_choice == "scissor":
    print(f"player wins! {player_choice} beats {computer_choice}.")

elif player_choice =="paper" and computer_choice == "rock":
    print(f"player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissor" and computer_choice == "paper":
    print(f"player wins! {player_choice} beats {computer_choice}.")

else:
    print(f"computer wins! {computer_choice} beats {player_choice}.")
