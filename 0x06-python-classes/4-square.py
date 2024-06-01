#!/usr/bin/python3
"""Define square a class"""


class Square:
    """Represents a square, with a private attribute"""

    def __init__(self, size=0):
        """Initialization of the object"""
        if not isinstance(size, int):
            return TypeError("size must be an integer")
        elif size < 0:
            return ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Using getter to retrieve the private attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Using setter to change the value of the priate attribute"""
        self.__size = value

    def area(self):
        """Public method that returns the area of the square"""
        return (self.__size * self.__size)
