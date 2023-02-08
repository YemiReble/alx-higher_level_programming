#!/usr/bin/python3
"""Importing from 7's BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherit from Base Geometry"""

    def __init__(self, width, height):
        """Initializing Rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() of this Rectangle"""
        strr = "[" + str(self.__class__.__name__) + "]"
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
