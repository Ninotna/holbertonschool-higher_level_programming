#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    safe_function - Executes a function safely
    @fct: A pointer to the function to be executed
    @args: Arguments to be passed to the function
    Return: The result of the function, or None if an exception occurs
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
