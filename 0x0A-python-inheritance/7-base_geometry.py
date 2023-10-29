#!/usr/bin/python3
""" This is no longer an empty class """


class BaseGeometry:
    """ This function is for geometry """

    def area(self):
        """ Defines the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks for type errors """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value
