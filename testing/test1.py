"""
Module: test1
This module contains utility functions for testing with doctest.
"""

def add(a, b):
    """
    Adds two numbers together.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)  # Set verbose=True to display all test results
