#!/usr/bin/python3
"""

This module is composed by a function that multiplies 2 matrices

"""

def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices m_a and m_b

    Args:
        m_a: first matrix, a list of lists of integers/floats
        m_b: second matrix, a list of lists of integers/floats

    Returns:
        A new matrix representing the product of m_a and m_b

    Raises:
        TypeError: If m_a or m_b is not a list, list of lists,
                   or if elements are not integers/floats,
                   or if rows are not of the same size.
        ValueError: If m_a or m_b is empty, or if they can't be multiplied.
    """

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate elements of m_a and m_b are integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate m_a and m_b are rectangular (all rows have the same size)
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate matrix multiplication compatibility (columns of m_a == rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply the matrices
    result = []
    for i in range(len(m_a)):  # Iterate through rows of m_a
        row_result = []
        for j in range(len(m_b[0])):  # Iterate through columns of m_b
            sum_product = 0
            for k in range(len(m_b)):  # Perform the dot product
                sum_product += m_a[i][k] * m_b[k][j]
            row_result.append(sum_product)
        result.append(row_result)

    return result
