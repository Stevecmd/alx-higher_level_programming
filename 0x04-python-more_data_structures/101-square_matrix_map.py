#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """Compute the square value of all integers in a matrix."""
    return list(map(lambda row: list(map(lambda element: element ** 2, row)), matrix))
