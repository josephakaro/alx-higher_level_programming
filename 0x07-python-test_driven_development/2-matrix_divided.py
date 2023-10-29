#!/usr/bin/python3

""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):

    """" this function divides all elements of a matrix """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    count = 0
    rows = 0
    col = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(error)

    flag = 0

    for y in matrix:
        if flag == 0:
            tmp = len(y)
            flag = 1
        else:
            if len(y) != tmp:
                raise TypeError(errortoolong)
        for x in y:

            if type(x) not in [int, float]:
                raise TypeError(errortoolong)
            count += 1

    new = list(map(lambda x:
                   list(map(lambda i: round(i / div, 2), x)), matrix))

    return (new)
