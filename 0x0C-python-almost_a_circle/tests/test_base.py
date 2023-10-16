#!/usr/bin/python3
""" module containts unit tests for class Base """


import unittest
import json

from models.base import Base


class TestBase(unittest.TestCase):
    """ unit tests for Base """

    @classmethod
    def setUp(self):
        """ tests id is at zero to start """
        Base._base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        b6 = Base()
        b7 = Base()

    def test_id(self):
        """ is id and id update functional """
        b1 = Base()
        self.assertEqual(b1.id, 10)

        b2 = Base(5)
        self.assertEqual(b2.id, 5)

        b3 = Base(89)
        self.assertEqual(b3.id, 89)

        b4 = Base(-5)
        self.assertEqual(b4.id, -5)

        b5 = Base(2)
        self.assertEqual(b5.id, 2)

        b6 = Base(None)
        self.assertEqual(b6.id, 11)

        b7 = Base(3.14)
        self.assertEqual(b7.id, 3.14)

    def test_rename(self):
        """ test rename id """
        b1 = Base(4)
        b1 = Base(-5)
        b1 = Base(2)
        self.assertEqual(b1.id, 2, "Should be 2")

    def test_for_none_to_json_string(self):
        """ test for none """
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_for_none_from_json_string(self):
        """ test for none """
        self.assertEqual(Base.from_json_string(None), [])

    def test_to_json_string(self):
        """ test JSON string conversion """
        b1_dict = {'id': 4, 'width': 5, 'height': 10, 'x': 3, 'y': 3}
        j_string = Base.to_json_string(b1_dict)
        t_d = json.loads(j_string)
        self.assertEqual(t_d, b1_dict)
        self.assertIs(type(j_string), str)
        self.assertIs(type(t_d), dict)
