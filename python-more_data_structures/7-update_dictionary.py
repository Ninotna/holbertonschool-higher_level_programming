#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    update_dictionary - Replaces or adds a key/value in a dictionary
    @a_dictionary: The input dictionary
    @key: The key to be added or updated (string)
    @value: The value to associate with the key (any type)
    Return: The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
