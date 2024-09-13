#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - Divides two integers and prints the result
    @a: The dividend
    @b: The divisor
    Return: The result of the division, or None if division by zero
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
