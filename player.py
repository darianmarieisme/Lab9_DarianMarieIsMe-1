'''Lab 9 Programming Assignment
Darian Marie Bruce
This is a class symbolizing a player
03/14/2026'''

import coin

class Player:

    def __init__(self,name: str):
        '''This method initializes the attributes for this class
        args:
            the object being used by the class
            the name as a string of the player
        '''

        self.__name: str = name

        self.__wallet: int = 20

        self.__coin = coin.Coin()

    def toss_coin(self):
        '''This method calls toss from coin on instance of coin class
        args:
            the object being used by the class
        '''
        self.__coin.toss()

    def get_coin_side(self):
        '''This method calls the method to get the coin side in string
        args:
            the object being used by the class
        '''
        return self.__coin.get_sideup()

    def win_coin(self):
        '''This method increments the wallet by an integer of one
        args:
            The object being used by the class
        '''
        self.__wallet += 1

    def lose_coin(self):
        '''This method decrements the wallet by an integer of one
        args: 
            the object being used by the class
        '''
        self.__wallet -= 1

    def get_wallet(self) -> int:
        '''This method returns the integers in the wallet
        args:
            the object being used by the class
        returns:
            private amount in wallet
        '''

        return self.__wallet
    
    def get_name(self) -> str:
        '''This method returns the string of the player
        args:
            the object being used by the class
        returns:
            private string naming player
        '''

        return self.__name