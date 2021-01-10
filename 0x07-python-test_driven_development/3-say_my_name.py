#!/usr/bin/python3
""" this is where modules go """


def say_my_name(first_name, last_name=""):
    """ this function prints a name """
    if type(first_name) is not in str:
        TypeError("first_name must be a string")
    if type(last_name) is not in str:
        TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
