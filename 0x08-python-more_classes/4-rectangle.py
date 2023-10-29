#!/usr/bin/python3
""" This module contains a Rectangle """


class Rectangle:
    """ Rectangle returns area and perimeter """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width or self.height is 0:
            return ("")
        for w in range(self.width):
            for h in range(self.height):
                print('#')

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return ((self.width * 2) + (self.height * 2))
        else:
            return 0
