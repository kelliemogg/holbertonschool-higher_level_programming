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
        if self.__width == 0 or self.__height == 0:
            return
        else:
            return self.__width * self.__height

    def display(self):
        """ display the rectangle using octothorps """
        if self.__width == 0 or self.__height == 0:
            print("")
        for y_axis in range(self.__y):
            print(" ")
        for col in range(self.__height):
            for x_axis in range(self.__x):
                print(" ", end="")
            for row in range(self.__width + 1):
                if row == self.__width:
                    print("", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """ string method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update attributes and assigns new arguments """
        for key, arg in enumerate(args):
            if key == 0:
                self.id = int(arg)
            elif key == 1:
                self.__width = int(arg)
            elif key == 2:
                self.__height = int(arg)
            elif key == 3:
                self.__x = int(arg)
            elif key == 4:
                self.__y = int(arg)
        if args is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = int(value)
                elif key == 'width':
                    self.__width = int(value)
                elif key == 'height':
                    self.__height = int(value)
                elif key == 'x':
                    self.__x == int(value)
                elif key == 'y':
                    self.__y == int(value)
