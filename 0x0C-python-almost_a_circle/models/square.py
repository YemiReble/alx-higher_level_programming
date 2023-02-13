#!/usr/bin/python3
"""Square Class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiatlizing Squares"""
        self.__size = size
        self.__x = x
        self.__y = y
        self.__id = None
        super().__init__(size, size, x, y, id)
