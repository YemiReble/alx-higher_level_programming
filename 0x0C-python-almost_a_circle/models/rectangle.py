#!/usr/bin/python3
""" A class that inherits from Base Class"""


from models.base import Base


class Rectangle(Base):
    """ A class that inherits from Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initaiting Reactangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """Getter Function List"""
    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @property
    def x(self):
        """Get the value of x"""
        return self.__x

    @property
    def y(self):
        """ Get the value of y"""
        return self.__y

    """Setter Function List"""
    """For width"""
    @width.setter
    def width(self, value):
        """Fucntion that set conditions for width and raise exceptions
        if values are not as expected"""
        if (type(value) is not int):
            # if not int(value):
            raise TypeError("{} must be an integer".format('width'))

        if value <= 0:
            raise ValueError("{} must be > 0".format('width'))

        self.__width = value

    """For height"""
    @height.setter
    def height(self, value):
        """Function that set conditions for height and raise exceptions
        if value are not as expected"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('height'))

        if value <= 0:
            raise ValueError("{} must be > 0".format('height'))

        self.__height = value

    @x.setter
    def x(self, value):
        """Function that set conditions for x value and raise exceptions if
        value are not as expected."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('x'))

        if value <= 0:
            raise ValueError("{} must be > 0".format('x'))

        self.__x = value

    @y.setter
    def y(self, value):
        """Function that set condition for y value and raise exceptions if
        value are not as expected."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format('y'))

        if value <= 0:
            raise ValueError("{} must be > 0".format('y'))

        self.__y = value

    def area(self):
        """ A Public method that retuns the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ Another public method that prints a regtangle with # sign"""
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """A method that does some calculations"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """A Public method that assign an argument to all attributes."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        obj_dictionary = {'id': self.id, 'width': self.__width,
                            'height': self.__height, 'x': self.__x,
                            'y': self.__y}
        return obj_dictionary
