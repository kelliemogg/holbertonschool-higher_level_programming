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

    def update(self, *args, **kwargs):
        """ update variables """
        for (key, arg) in enumerate(args):
            if key == 0:
                self.id = int(arg)
            elif key == 1:
                self.size = int(arg)
            elif key == 2:
                self.x = int(arg)
            elif key == 3:
                self.y = int(arg)
        if args is not None:
            for (key, value) in kwargs.items():
                if key == 'id':
                    self.id = int(value)
                elif key == 'size':
                    self.size = int(value)
                elif key == 'x':
                    self.x = int(value)
                elif key == 'y':
                    self.y = int(value)
