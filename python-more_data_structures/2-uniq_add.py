#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    uniq_add - Adds all unique integers in a list
    @my_list: The list of integers
    Return: Sum of unique integers
    """
    return sum(set(my_list))
