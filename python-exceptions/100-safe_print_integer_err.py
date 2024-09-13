#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    safe_print_integer_err - Prints an integer, handles errors, and prints them to stderr
    @value: The value to be printed, which can be of any type
    Return: True if value is correctly printed as an integer, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
