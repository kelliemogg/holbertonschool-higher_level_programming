#!/usr/bin/python3
""" module containts unit tests for class Rectangle """


import unittest
import json

from models.rectangle import Rectangle


class RectangleBase(unittest.TestCase):
    """ unit tests for class Rectangle """

    @classmethod
    def setUp(self):
        """ check that rect id is zeroed out """
        Rectangle._rectangle__nb_objects = 0

#    def test_rectangle_args(self):
#        """ number of args """
#        r1 = Rectangle(1, 2, 3, 4, 5, 6)
#        self.assertEqual(r1.6)

    def test_var_matches(self):
        """ matching variables """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)
