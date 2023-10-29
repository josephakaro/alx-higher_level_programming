#!/usr/bin/python3
""" function that adds 2 integers """


def add_integer(a, b=98):

    """ function that adds 2 integers """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
