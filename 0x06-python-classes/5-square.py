#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Square class with private size attribute, validation, area, and my_print methods."""

    def __init__(self, size=0):
        """Initialize the Square instance with an optional size."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute."""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square using '#' characters."""

        printSize = self.__size
        if printSize == 0:
            print()
        for i in range(printSize):
            for j in range(printSize):
                print("#", end="")
            print()
