import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print("")
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: ")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1,2 or 3.")

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

    if player == 1 and computer == 3:
        print("😜 You win!")
    elif player == 2 and computer == 1:
        print("😜 You win!")
    elif player == 3 and computer == 2:
        print("😜 You win!")
    elif player == computer:
        print("🙌 Tie game!")
    else: 
        print("🤷‍♂️ Computer wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ for Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\nThank you for playing!🎉🎉🎉\n")
        playagain = False