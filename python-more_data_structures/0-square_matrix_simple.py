#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - Computes the square value of all integers
    @matrix: A 2 dimensional array of integers
    Return: A new matrix with squared values
    """
    return [[x ** 2 for x in row] for row in matrix]
