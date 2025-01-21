# scissor paper rock

import random
game_list=["ROCK","PAPER","SCISSOR"]

menu="""
       WELCOME TO ROCK PAPER SCISSOR GAME

       PRESS ROCK 
       PRESS PAPER 
       PERSS SCISSOR 
    """
status=True
while status:
    print(menu)
    computer=random.choice(game_list)
    user_choice=input("enter your choice:").upper()
    print("computer choice:",computer)
    print("user_choice:",user_choice)
    print()
    if user_choice=="ROCK" and computer=="PAPER"or user_choice=="PAPER" and computer=="SCISSOR" or user_choice=="SCISSOR" and computer=="ROCK":
        print("computer won this match")
    elif user_choice=="ROCK" and computer=="SCISSOR" or user_choice=="PAPER" and computer=="ROCK" or user_choice=="SCISSOR" and computer=="PAPER":
        print("user won this match!!")
    else:
        print("tie")

    choice =input("do you want to play again press 'y' for yes and press 'n' for no:")  
    if choice=='n' and choice=='no':
        status =False   