#!/usr/bin/python3
"""
    function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    if type(matrix) not in [int, float]:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')