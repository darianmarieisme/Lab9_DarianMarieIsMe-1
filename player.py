'''Lab 9 Programming Assignment
Darian Marie Bruce
This is a class symbolizing a player
03/14/2026'''

import coin

class Player:

    def __init__(self,name: str):

        self.__name: str = name

        self.__wallet: int = 20

        self.__coin = coin.Coin()