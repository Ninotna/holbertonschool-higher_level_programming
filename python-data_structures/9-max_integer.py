def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Args:
    my_list (list): A list of integers.

    Returns:
    int or None: The largest integer in the list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    max_val = my_list[0]  # Initialize max_val with the first element of the list

    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
