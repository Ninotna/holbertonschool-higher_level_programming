#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all integers in a list, one per line.

    Args:
    my_list (list): A list of integers.

    Example:
    >>> print_list_integer([1, 2, 3])
    1
    2
    3
    """
    for element in my_list:
        print("{:d}".format(element))
