#!/usr/bin/python3
""" This is no longer an empty class """


class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
