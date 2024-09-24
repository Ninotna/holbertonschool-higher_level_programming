#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    is_same_class - returns True if object is exactly an instance of
    the specified class; otherwise False
    @obj: the object to check
    @a_class: the class to match the type of obj to
    Return: True if obj is an instance of a_class, otherwise False
    """
    return (type(obj) == a_class)

