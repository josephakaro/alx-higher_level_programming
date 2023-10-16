#!/usr/bin/python3
"""
    Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherit from Base Class """
    def __init__(self, width, height, x=0, y=0,id=None):
        """ Redundun function (Initilliazier) """
        super().__init__(id)
        self.width = width
        self.width = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ Returns private getter for width """
        return self.__width
    
    @property
    def height(self):
        """ Returns private getter for height """
        return self.__height

    @property
    def x(self):
        """ Returns private getter for x"""
        return self.__x
    
    @property
    def y(self):
        """ Returns private getter for y"""
        return self.__y
    
    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        else:
            self.__width = value
    
    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 1:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value
    
    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
    
    def area(self):
        """ gets the area of a Rectangle """
        if self.__width == 0 or self.__height == 0:
            return
        else:
            return self.__width * self.__height

    def display(self):
        """ Function """
        if self.__width == 0 or self.__height == 0:
            print("")
        for y_axis in range(self.__y):
            print("")
        for col in range(self.__height):
            for x_axis in range(self.__x):
                print(" ", end="")
            for row in range(self.__width):
                if row == self.__width:
                    print("", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """ string method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update attributes and assigns new arguments """
        for (k, arg) in enumerate(args):
            if k == 0:
                self.id = int(arg)
            elif k == 1:
                self.__width = int(arg)
            elif k == 2:
                self.__height = int(arg)
            elif k == 3:
                self.__x = int(arg)
            elif k == 4:
                self.__y = int(arg)
        if args is not None:
            for (key, value) in kwargs.items():
                if key == 'id':
                    self.id = int(value)
                elif key == 'width':
                    self.__width = int(value)
                elif key == 'height':
                    self.__height = int(value)
                elif key == 'x':
                    self.__x = int(value)
                elif key == 'y':
                    self.__y = int(value)

    def to_dictionary(self):
        """ dict representation of a rectangle """
        var_dict = ({'id': self.id, 'width': self.__width, 'height':
                     self.__height, 'x': self.__x, 'y': self.__y})
        return var_dict  