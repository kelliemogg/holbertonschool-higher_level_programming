#!/usr/bin/python3
""" class that inherits from Base class """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ this initializes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 1:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """ setter for x """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ gets the area of a Rectangle """
        return self.__width * self.__height

    def display(self):
        """ display the rectangle using octothorps """
        if self.__width is 0:
            print("")
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    print("#".format(self), end="")
                print("")
