#!/usr/bin/python3
""" module containts unit tests for class Square """


import unittest
import json

from models.square import Square


class SquareBase(unittest.TestCase):
    """ unit tests for class Square """

    @classmethod
    def setUp(self):
        """ check that base id is zeroed out """
        Square._square__nb_objects = 0

    def test_rectangle_not_square(self):
        """ sq not rect """
        s1 = Square(5, 5, 1, 1)
        self.assertEqual(s1.width, s1.height)

    def test_var_matches(self):
        """ matching variables """
        s1 = Square(6, 7, 8, 9)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 9)

    def test_square_args(self):
        """ number of args """
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5, 6)
            s2 = Square(1, 4, 3)
            s3 = Square(0, 1, 1, 3.5)
            s4 = Square("", 1, 1, 3)
            s5 = Square(9, 4, 4, 5)
            s6 = Square("lol", -3, 1, 2)
            s7 = Square(-2, -3, -4, -6)
            s8 = Square(1, 2)
            s8 = Square(4)
            s9 = Square("reishi")