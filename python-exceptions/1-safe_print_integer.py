#!/usr/bin/python3
def safe_print_integer(value):
    """
    safe_print_integer - Prints an integer using "{:d}".format()
    @value: The value to print, which can be of any type
    Return: True if value is correctly printed as an integer, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
