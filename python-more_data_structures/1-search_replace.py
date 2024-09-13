#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - Replaces all occurrences of an element by another
    @my_list: The initial list
    @search: The element to be replaced
    @replace: The new element
    Return: A new list with replaced elements
    """
    return [replace if x == search else x for x in my_list]
