#!/usr/bin/python
"""
    Unit Test for base classes
"""

import unittest
from models.base import Base

class TestBaseMode(unittest.TestCase):
    """
        Testing Base module for any exception raises as neccesary
    """
    def test_type(self):
        self.assertRaises(TypeError, Base().id)
        self.assertRaises(TypeError, Base().id)
        self.assertRaises(TypeError, Base().id)
        self.assertRaises(TypeError, Base(12).id)
        self.assertRaises(TypeError, Base().id)
    
    def test_true(self):
        self.assertTrue(Base().id, 1)
        self.assertTrue(Base().id, 2)
        self.assertTrue(Base().id, 3)
        self.assertTrue(Base(12).id, 12)
        self.assertTrue(Base().id, 4)

if __name__ == '__main__':
    unittest.main()