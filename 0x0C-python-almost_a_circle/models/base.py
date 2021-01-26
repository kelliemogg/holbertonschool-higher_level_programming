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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep to a file """
        cls_name = cls.__name__ + ".json"
        list_dict = []

        if list_objs is None:
            list_objs = []

        for item in list_objs:
            list_dict.append(item.to_dictionary())

        with open(cls_name, 'w') as f:
            f.write(cls.to_json_string(list_dict))

