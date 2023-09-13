#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[a ** 2 for a in b] for b in matrix]
    return new_matrix
