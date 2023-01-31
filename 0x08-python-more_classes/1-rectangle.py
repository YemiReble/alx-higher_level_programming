#!/usr/bin/python3
"""An class Rectangle that defines a rectangle"""


class Rectangle:
    """A defined class that represents rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width: represent the width of a regtangle
            height: represent the height of a rectangle
        Errors:
            Raise:
                TypeError: if value is not an integer
                ValueError: if value is less than zero"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve width instance attribute"""
        return self.__width

    def width(self, value):
        """Making sure value is an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height instance attribute"""
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
