#!/usr/bin/python3
"""Importing from 7's BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherit from Base Geometry"""

    def __init__(self, width, height):
        """Initializing Rectangle"""

        self.integer_validator("width", height)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        strr = "[" + str(self.__class__.__name__) + "]"
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
