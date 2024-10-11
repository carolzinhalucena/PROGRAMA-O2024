import math

class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def delta (self):
        retun self.__b**2 - 4 * self.__a * self.__c 

    def __str__(self):
        return f'Delta = '
