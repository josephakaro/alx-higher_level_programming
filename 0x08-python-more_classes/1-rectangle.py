#!/usr/bin/python3
"""
    Class that defines Rectangle with paramters width
"""


class Rectangle:
    """ 
        Rectangle class
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
            Defines the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width value validation
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    def height(self):
        """
            Defines the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
            Height value validation
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
