#!/usr/bin/python3
""" This is no longer an empty class """


class BaseGeometry:
    """ This function is for geometry """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def area(self):
        """ Defines the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks for type errors """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value


class Rectangle(BaseGeometry):
    """ Applies geometry to Rectangles """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """ Checks for type errors """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value

class Square(Rectangle):
    """ Applies geo to Square """
    def __init__(self, size):
        self.size = size

    def integer_validator(self, name, value):
        """ Checks for type errors """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value

        def area(self):
            """ Defines the area """
            raise Exception("area() is not implemented")