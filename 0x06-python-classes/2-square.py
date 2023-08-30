#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Square class with private size attribute and validation."""

    def __init__(self, size = 0):
        """Initialize the Square instance with an optional size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
