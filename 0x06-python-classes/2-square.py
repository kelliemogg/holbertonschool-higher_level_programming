#!/usr/bin/python3

""" Module Goes Here """


class Square:
    """ Sq Class defines sq by size, a private instance attribute """
    def __init__(self, size=0):
        try:
            print("{:d}".format(size))
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
