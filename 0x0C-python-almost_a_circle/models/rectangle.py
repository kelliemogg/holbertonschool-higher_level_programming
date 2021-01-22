#!/usr/bin/python3
""" class that inherits from Base class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class inheriting from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        elif not isinstance(width, int):
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if isinstance(x, int):
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if isinstance(y, int):
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
