#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    complex_delete - Deletes keys with a specific value in a dictionary
    @a_dictionary: The dictionary to modify
    @value: The value to search for and delete keys associated with it
    Return: The updated dictionary
    """
    # Create a list of keys to delete
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]

    # Delete the identified keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
