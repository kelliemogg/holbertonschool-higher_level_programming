#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ is an obj a subclass of the specified class """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
