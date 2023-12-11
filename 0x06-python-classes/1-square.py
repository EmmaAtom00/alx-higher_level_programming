#!/usr/bin/python3

"""Declaring a class with a private attribute size"""


class Square:
    """The square object and attributes goes here"""

    def __init__(self, size):
        """
            Initialize a new size
            Args:
                size (int): new size of the square
        """
        self.__size = size
