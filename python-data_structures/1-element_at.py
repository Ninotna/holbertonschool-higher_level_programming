#!/usr/bin/python3

def element_at(my_list, idx):
    """
    element_at - retrieves an element from a list at a specific index
    @my_list: list to retrieve the element from
    @idx: index of the element to retrieve
    Return: element at index idx, or None if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
