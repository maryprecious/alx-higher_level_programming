#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Write A function that computes the square
    value of all integers of a matrix.
    """
    mysquared_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        mysquared_matrix.append(result)
    return mysquared_matrix
