#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elements of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    # Ensure the matrix is a list of lists and that
    # the lists contain integers/floats
    if not isinstance(matrix, list) or len(matrix) == 0
    or not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg_type)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg_type)  # Empty row raises a matrix type error
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(msg_type)

    # Check that all rows have the same size after validating contents
    len_e = len(matrix[0])
    for row in matrix:
        if len(row) != len_e:
            raise TypeError(msg_size)

    # Perform the division
    return [[round(num / div, 2) for num in row] for row in matrix]
