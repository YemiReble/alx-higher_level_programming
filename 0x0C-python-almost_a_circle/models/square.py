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

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    """Setter and Getter"""
    @property
    def size(self):
        """Getting the value of size"""
        return self.__size

    @property
    def x(self):
        """getting the value of x"""
        return self.__x

    @property
    def y(self):
        """Getting the value of y"""
        return self.__y

    """Setter"""
    @size.setter
    def size(self, value):
        """Function that set the value of size conditions to raise
        exceptions"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
