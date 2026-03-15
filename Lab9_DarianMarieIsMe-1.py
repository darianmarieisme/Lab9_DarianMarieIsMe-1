'''Lab 9 Programming Assignment
Darian Marie Bruce
This is a matching coin game
03/14/2026'''

import player

#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
purple: str = "\033[38;5;129m"
green: str = "\033[38;5;46m"
reset: str = "\033[0m"

def toss_coin()

    play = input(f"{purple}Do{reset} you want to toss the coins? (y/n):").lower()

    if play == "y":

    else:
        continue
    
    

def main() -> None:
    
    player1 = player("Player 1")

    player2 = player("Player 2")

    game = True

    print(f"-"*3,"Coin {purple}Match{reset} Game","-"*3)

    while game == True:
        gamestatus: str = input(f"{purple}Do{reset} you want to toss the coins? (y/n):").lower()

        if gamestatus == "y":
            
            print("Tossing...")

            pass

        elif gamestatus == "n":
            
            game = False

        else: 
            print("Input is invalid. Please try again.")
            continue

