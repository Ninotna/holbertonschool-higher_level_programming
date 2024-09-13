#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - prints all integers of a list in reverse order
    @my_list: list of integers to be printed
    Return: None
    """
    my_list.reverse()

    for element in my_list:
        print("{:d}".format(element))
