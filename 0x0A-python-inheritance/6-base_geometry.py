#!/usr/bin/python3
""" This is no longer an empty class """


class BaseGeometry:
    """ This class is of geometry """
    def area(self):
        """ gathers area of a shape """
        raise Exception("area() is not implemented")
