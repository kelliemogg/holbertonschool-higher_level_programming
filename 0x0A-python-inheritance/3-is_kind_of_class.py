#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ T or F if obj is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False