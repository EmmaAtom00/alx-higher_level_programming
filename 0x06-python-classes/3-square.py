#!/usr/bin/python3

"""Define a Square class with exception in validation"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        Initializes a new square
        Args:
            size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the squre"""
        return self.__size * self.__size
