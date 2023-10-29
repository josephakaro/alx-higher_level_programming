#!/usr/bin/python3
""" This module tests for matching classes """


def is_same_class(obj, a_class):
    """ T or F for the instance of an obj of a class """
    if type(obj) is a_class:
        return True
    else:
        return False
