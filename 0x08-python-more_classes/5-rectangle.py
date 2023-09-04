#!/usr/bin/python3
"""

Class Rectangle that defines a rectangle

"""


class Rectangle:
    """
    Create Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize variables
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        returns width value
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        method to get area
        """
        return self._width * self._height

    def perimeter(self):
        """
        method to get perimeter
        """
        return self._width * 2 + self._height * 2

    def __str__(self):
        """
        print rectangle using #
        """
        string = ""
        if self._width == 0 or self._height == 0:
            string += "\n"
            return
        for i in range(self._height):
            string += "#" * self._width + "\n"
        return string[:-1]

    def __repr__(self):
        """
        print string representing width and height of rectangle
        """
        string = "Rectangle(" + str(self._width) + ", " + str(self._height) + ")"
        return string

    def __del__(self):
        """
        deletes rectangle
        """
        print("Bye rectangle...")
