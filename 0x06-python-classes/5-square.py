#!/usr/bin/python3
""" Module Goes Here """


class Square:
    """ Sq Class defines sq by size, a private instance attribute """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")

    def area(self):
        area = (self.__size) * (self.__size)
        return(area)

    def my_print(self):
        if self.__size is 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#".format(self.__size), end="")
                print("")
#                print("#".format(self.__size), end="")
