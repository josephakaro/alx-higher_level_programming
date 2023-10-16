#!/usr/bin/python3
"""
    Class base
"""

class Base:
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ Initilizer with Class and ID """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
