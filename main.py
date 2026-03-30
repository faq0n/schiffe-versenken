from ship import Ship
import os


def main():

    pos1 = ""
    pos2 = ""

    def place_prompt():
        placement = input("Where do you want to place your ship (A,1): ")
        positioning = placement.split(",")
        pos1, pos2 = positioning
        return pos1, pos2

    shipRed = Ship("A3", "A6", 1)
    print("Player 1 turn \n")
    gameState = ""
    if shipRed.get_sunken == True:
        gameState = "won"
    else:
        gameState = "not decided"


main()
