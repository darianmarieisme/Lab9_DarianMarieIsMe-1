'''Lab 9 Programming Assignment
Darian Marie Bruce
This is a matching coin game
03/14/2026'''

from player import Player

#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
purple: str = "\033[38;5;129m"
green: str = "\033[38;5;46m"
reset: str = "\033[0m"
    

def main() -> None:
    
    player1 = Player(f"Player {orange}1{reset}")

    player2 = Player(f"Player {orange}2{reset}")

    game: bool = True

    print("-"*3,f"Coin {purple}Match{reset} Game","-"*3)

    while game == True:
        gamestatus: str = input(f"{purple}Do{reset} you want to toss the coins? (y/n):").lower()

        if gamestatus == "y":
            
            print("Tossing...")

            player1.toss_coin()
            player2.toss_coin()

            p1_turn: str = player1.get_coin_side()
            p2_turn: str = player2.get_coin_side()

            print(f"{player1.get_name()} tossed {p1_turn}\n{player2.get_name()} tossed {p2_turn}")

            if p1_turn == p2_turn:

                print(f"...It{green}'s a Match! Player 1 wins a coin.{reset}")

                player1.win_coin()
                player2.lose_coin()

                p1_wallet: int = player1.get_wallet()
                p2_wallet: int = player2.get_wallet()

                print(f"{green}Player 1 has {p1_wallet} coin(s).\nPlayer 2 has {p2_wallet} coin(s).")

            else:

                print(f"No {purple}Match{reset}! Player {orange}2{reset} wins a coin.")

                player1.lose_coin()
                player2.win_coin()

                p1_wallet: int = player1.get_wallet()
                p2_wallet: int = player2.get_wallet()

                print(f"{player1.get_name()} has {orange}{p1_wallet}{reset} coin(s).\n{player2.get_name()} has {orange}{p2_wallet}{reset} coin(s).")

        elif gamestatus == "n":
            
            p1_wallet: int = player1.get_wallet()
            p2_wallet: int = player2.get_wallet()

            print(f"{green}-"*3,"Final Score","-"*3)
            print(f"{green}Player 1: {p1_wallet}\nPlayer 2: {p2_wallet}")

            if p1_wallet == p2_wallet:

                print(f"{green}It's a draw!{reset}")

                game = False

            elif p1_wallet > p2_wallet:

                print(f"{green}Player 1 wins!{reset}")

            else:

                print(f"{green}Player 2 wins!{reset}")

                game = False


        else: 
            print("Input is invalid. Please try again.")
            continue


if __name__ == "__main__":
    main()