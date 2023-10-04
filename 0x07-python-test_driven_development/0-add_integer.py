#!/usr/bin/python
""" Function that sum two integers """

def add_integer(a, b=98):
    """ Sum two integer """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
