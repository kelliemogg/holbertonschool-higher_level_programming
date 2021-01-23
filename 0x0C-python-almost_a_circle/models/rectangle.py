#!/usr/bin/python3
""" class that inherits from Base class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class inheriting from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
