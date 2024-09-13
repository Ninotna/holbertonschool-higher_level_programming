#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.

    Args:
    my_list (list): The list to work with.
    idx (int): The index of the element to replace.
    element: The new element to be placed in the list.

    Returns:
    list: A new list with the element replaced if idx is valid, otherwise a copy of the original list.
    """
    #  Create a real copy of a list (not just reference)
    new_list = my_list[:]

    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element

    return new_list
