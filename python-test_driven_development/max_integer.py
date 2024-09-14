#!/usr/bin/python3

def max_integer(list=[]):
    """Function to find and return the maximum integer in a list of integers.
    If the list is empty, it returns None.
    """
    if len(list) == 0:
        return None
    return max(list)
