## create game "rock-paper-scissors" with Python

import random

def Rock_Paper_Scissors():
    win = 0
    lose =0
    tie = 0

    actions = ["r","p","s"]

    while True :
        print("Choose your move: type r for Rock, p for Paper, s for Scissors, and x for Exit" )
        player_move = input("player_move: ")
        com_move = random.choice(actions)

       
        if player_move == "x":
            print("---Goodbye :D --- Your score is")
            print(f"Win: {win}  Lose: {lose}  Tie: {tie}")
            
            break

        if(com_move == player_move):
            print(f"Computer move: {com_move}")
            print("---Tie----")
            tie +=1

        elif(player_move =="r" and com_move =="s"):
           print("Computer move: Scissors")
           print("player move: Rock")
           print("---You win---")
           win +=1

        elif(player_move =="s" and com_move =="p"):
           print("Computer move: Paper")
           print("player move: Scissors")
           print("---You win---")
           win +=1

        elif(player_move =="p" and com_move =="r"):
           print("Computer move: Rock")
           print("player move: Paper")
           print("---You win---")
           win +=1

        else:
            print(f"Computer move {com_move}")
            print("---You lose---")
            lose +=1
        
