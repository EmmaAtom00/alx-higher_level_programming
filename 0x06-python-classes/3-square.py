#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing the class"""

        if not isinstance(size, int):
            return TypeError("size must be an integer")

        elif size < 0:
            return ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        ARGS:
            self (int): the instance of the class with a property size
        """

        return self.__size * self.__size
