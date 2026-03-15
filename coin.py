'''Lab 9 Programming Assignment
Darian Marie Bruce
This is a class symbolizing a tossable coin with two
states: heads or tails
03/14/2026'''

import random

class Coin:
    
    def __init__(self):
        '''Initializes a private string for use in the class
        args:
            the object using the method
        '''
        self.__sideup: str = "Heads"

    def toss(self):
        '''Calls a random integer to assign to the object
        args:
            the object using the method
        '''
        number: int = random.randint(0,1)

        if number == 0:

            self.__sideup = "Heads"

        else:

            self.__sideup = "Tails"

    def get_sideup(self):
        '''Method to return the "heads or "tails" string
        args:
            the object using the method
        returns:
            the private state of the coin "heads" or "tails"
        '''
        return self.__sideup


