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

    def test_rectangle_args(self):
        """ number of args """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)
            r2 = Rectangle(1, 0, 3, 4)
            r3 = Rectangle(0, 1, 2, 3.5)
            r4 = Rectangle("", 1, 1, 3)
            r5 = Rectangle(9, -3, 4, 5)
            r6 = Rectangle("lol", -3, 1, 2)
            r7 = Rectangle(-2, -3, -4, -6)
            r8 = Rectangle(1, 2)
            r8 = Rectangle(4)
            r9 = Rectangle("reishi")

    def test_var_matches(self):
        """ matching variables """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)