#!/usr/bin/python3
""" This module is of class Base """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ this is class Square inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ output of square attributes """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
