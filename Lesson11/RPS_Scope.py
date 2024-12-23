import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("")
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: ")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2 or 3.")
        play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    # print("You chose " + playerchoice + ".")
    # print("Computer chose " + computerchoice +".")
    # print("You chose " + str(RPS(player)) + ".")
    # print("Computer chose " + str(RPS(computer)) +".")
    print("You chose " + str(RPS(player)).replace("RPS.","") + ".")
    print("Computer chose " + str(RPS(computer)).replace("RPS.","") +".")
    print("")

    def decide_winner(player,computer):

        if player == 1 and computer == 3:
            return "😜 You win!"
        elif player == 2 and computer == 1:
            return "😜 You win!"
        elif player == 3 and computer == 2:
            return "😜 You win!"
        elif player == computer:
            return "🙌 Tie game!"
        else: 
            return "🤷‍♂️ Computer wins!"
    
    game_results = decide_winner(player,computer)
    print(game_results)

    global game_count
    game_count += 1

    print("\nGame count " + str(game_count))

    print("\nPlay again?")

    while True:

        playagain = input("\nY for Yes or \nQ for Quit\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you for playing!🎉🎉🎉\n")
        sys.exit("Bye! 🙌")
        
play_rps()