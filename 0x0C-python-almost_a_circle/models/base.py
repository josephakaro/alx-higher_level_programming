#!/usr/bin/python3
"""
    This module holds Base Class of all Classes in this project files.\
    It is aimed at managing id attributes of all future classes and avoid at duplicating same code.
"""

class Base:
    """ Base class """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ Initilizier function with private attributes and id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
