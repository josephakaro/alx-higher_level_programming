#!/usr/bin/python3
""" Function that adds 2 integers """



def add_integer(a, b=98):
    """Function that adds two integers a and b."""
    if a is None or type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
