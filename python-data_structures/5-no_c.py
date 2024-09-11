def no_c(my_string):
    """
    no_c - removes all characters 'c' and 'C' from a string
    @my_string: the string to modify
    Return: a new string with 'c' and 'C' removed
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
