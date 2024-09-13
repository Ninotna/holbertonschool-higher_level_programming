#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - Prints x elements of a list
    @my_list: The input list which can contain any type
    @x: The number of elements to print
    Return: The actual number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()  # for new line after printing elements
    return count
