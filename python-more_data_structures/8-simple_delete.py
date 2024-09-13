#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    simple_delete - Deletes a key in a dictionary
    @a_dictionary: The input dictionary
    @key: The key to be deleted (string)
    Return: The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
