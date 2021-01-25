#!/usr/bin/python3
""" base module to manage id attributes in future classes"""


import json


class Base:
    """ This class will be the base for all other classes in this project """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ initializes base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries, default = str)
            return json_string
