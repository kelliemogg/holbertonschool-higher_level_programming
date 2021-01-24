#!/usr/bin/python3
""" This module is of class Base """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ this is class Square inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        else:
            self.__size = value

    def __str__(self):
        """ output of square attributes """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
