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
