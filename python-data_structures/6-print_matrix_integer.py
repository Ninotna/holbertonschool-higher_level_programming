#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - prints a matrix of integers
    @matrix: list of lists containing integers
    Return: None
    """
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()  # Move to the next line after each row
