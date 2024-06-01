#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents an object square, with setters and getters"""

    def __init__(self, size=0):
        """Initilize the class
        Args:
            size (int): the size of the square
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Change the value of the private attribute size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return self.__size * self.__size
