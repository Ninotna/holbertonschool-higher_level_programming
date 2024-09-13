#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - Prints the first x integers from a list
    @my_list: The input list containing any type of values
    @x: The number of elements to access from my_list
    Return: The number of integers printed
    """
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        pass
    print()  # for new line after printing integers
    return count
