#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    Arguments:
    matrix: lists of integers or floats
    div: number (integer or float)
    Return:
    All elements of the matrix divided by div
    """
    mtype = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(mtype)
    if len(matrix[0]) == 0:
        raise TypeError(mtype)
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(mtype)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for n in matrix:
        x = 0
        if len(n) != len(matrix[0]):
            raise TypeError("Each n of the matrix must have the same size")
        for x in n:
            if isinstance(x, (int, float)):
                x = int(x)
            else:
                raise TypeError(mtype)
    return [[round(x / div, 2) for x in n] for n in matrix]
