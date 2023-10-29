#!/usr/bin/python3
""" Module tests for what type an obj is """


def is_kind_of_class(obj, a_class):
    """ T or F if obj is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
