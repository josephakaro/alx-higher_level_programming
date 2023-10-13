#!/usr/bin/python3
"""
    function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides all items in a matrix """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    count = 0
    rows = 0
    col = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(msg)

    flag = 0

    for j in matrix:
        if flag == 0:
            tmp = len(j)
            flag = 1
        else:
            if len(j) != tmp:
                raise TypeError("errortoolong")
        for x in j:

            if type(x) not in [int, float]:
                raise TypeError("errortoolong")
            count += 1

    new = list(map(lambda i:
                   list(map(lambda i: round(i / div, 2), i)), matrix))

    return new
