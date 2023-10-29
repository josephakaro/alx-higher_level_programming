#!/usr/bin/python3
""" This is no longer an empty class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Applies geometry to Rectangles """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ string """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """ define area of obj """
        return self.__width * self.__height
