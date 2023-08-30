#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Initialize the Square instance with an optional size."""

    def __init__ (self, size = 0):
        """Initialize the Square instance with an optional size."""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2
