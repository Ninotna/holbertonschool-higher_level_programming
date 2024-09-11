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
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]  # Create a shallow copy of the list
    new_list[idx] = element
    return new_list
