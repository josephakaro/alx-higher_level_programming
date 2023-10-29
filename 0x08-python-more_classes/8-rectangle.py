#!/usr/bin/python3
""" This module contains a Rectangle """


class Rectangle:
    """ Rectangle returns area and perimeter
    prints out #'s to demonstrate the area
    prints when it is deleted
    keeps track of instances"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        if self.width or self.height is 0:
            return ("")
        for w in range(self.width):
            for h in range(self.height):
                print(self.print_symbol)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

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

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1 == rect_2:
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return ((self.width * 2) + (self.height * 2))
        else:
            return 0
