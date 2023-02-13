#!/usr/bin/python3
""" A class that inherits from Base Class"""


Rectangle = __improt__('base').Base

class Rectangle(Base):
    """ A class that inherits from Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initaiting Reactangle"""
        self.__width = width
        self.__height = height

