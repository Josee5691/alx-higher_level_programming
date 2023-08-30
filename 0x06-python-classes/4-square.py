#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Initialize the Square instance with an optional size."""

    def __init__(self, size = 0):
        """Initialize the Square instance with an optional size."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
