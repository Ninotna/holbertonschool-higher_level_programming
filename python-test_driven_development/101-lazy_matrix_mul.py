#!/usr/bin/python3
"""

This module is composed by a function that multiplies 2 matrices
by using numpy

"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy's matmul.

    Args:
        m_a: first matrix, a list of lists of integers/floats
        m_b: second matrix, a list of lists of integers/floats

    Returns:
        A new matrix representing the product of m_a and m_b

    Raises:
        TypeError: If m_a or m_b is not a list, or elements are not integers/floats,
                   or if rows are not of the same size.
        ValueError: If m_a or m_b is empty or they can't be multiplied.
    """

    # Ensure m_a and m_b are lists of lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check for empty matrices
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Ensure all elements are either integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check that each row has the same size in both matrices
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Attempt matrix multiplication using NumPy
    try:
        result = np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    return result.tolist()
