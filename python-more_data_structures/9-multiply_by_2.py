#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiply_by_2 - Returns a new dictionary with all values multiplied by 2
    @a_dictionary: The input dictionary with integer values
    Return: A new dictionary with values multiplied by 2
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
