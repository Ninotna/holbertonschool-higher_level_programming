def replace_in_list(my_list, idx, element):
    """
    replace_in_list - replaces an element of a list at a specific position
    @my_list: list where the replacement will happen
    @idx: index at which the element will be replaced
    @element: the new element to insert at the specified position
    Return: the modified list or the original list if idx is out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
