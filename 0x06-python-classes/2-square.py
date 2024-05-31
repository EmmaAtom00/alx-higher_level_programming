#!/usr/bin/python3
"""Defines a square by size using a private attribute and handling exception errors"""


class Square:
    """Represents a square, with a private attribute"""

    def __init__(self, size=0):
        """Initializing square size"""

        if not isinstance(size, int):
            # Check whether size has the type integer
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
