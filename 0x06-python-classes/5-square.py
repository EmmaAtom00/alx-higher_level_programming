#!/usr/bin/python3
"""Define a square, with private attributes"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the class
        Args:
            size (int): the size of the square
        """

        self.size = size

    @property
    def size(self):
        """Get the value of the priate attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Change the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for v in range(self.size):
                print("#", end="")
            print("")
