#!/usr/bin/python3
'''
Module for matrix_divided method
it divides all elements of a matrix
returns the new matrix
'''


def matrix_divided(matrix, div):
    '''
    Function that  divides all elements of a matrix.
    '''
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            result = round((elem / div), 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
