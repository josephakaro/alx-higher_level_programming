#!/usr/bin/python3
""" module """

class Student:
    """ class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            for i in self.__dict__:
                    d[i] = self.__dict__[i]
        return d
