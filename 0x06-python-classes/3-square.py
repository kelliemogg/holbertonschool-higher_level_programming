#!/usr/bin/python3
""" Module Goes Here """


class Square:
    """ Sq Class defines sq by size, a private instance attribute """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        area = (self.__size) * (self.__size)
        return(area)
