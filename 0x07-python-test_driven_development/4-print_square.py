#!/usr/bin/python3
""" function that adds 2 integers """


def print_square(size):
    """ function that prints a square """

    if not isinstance(size, int) or size is None:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            if b == size - 1:
                print("#")
            else:
                print("", end="")
