#!/usr/bin/python3
""" module """


def save_to_json_file(my_obj, filename):
    """ return func that writes an obj to a text file """
    import json
    return json.dumps(my_obj, ensure_ascii=False)
