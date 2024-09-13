#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print_sorted_dictionary - Prints a dictionary sorted by keys
    @a_dictionary: The input dictionary
    Return: None
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
