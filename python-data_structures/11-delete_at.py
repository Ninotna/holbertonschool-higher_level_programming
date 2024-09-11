def delete_at(my_list=[], idx=0):
    """
    delete_at - deletes the item at a specific position in a list
    @my_list: the list of items
    @idx: index of the item to delete
    Return: the modified list or the original list if idx is out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
