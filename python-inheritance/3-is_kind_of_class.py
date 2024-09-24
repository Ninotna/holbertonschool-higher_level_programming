#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - returns True if object is an instance of, or if
    the object is an instance of a class that inherited from, the specified class
    @obj: the object to check
    @a_class: the class or parent class to match the type of obj to
    Return: True if obj is an instance or inherited instance of a_class, else False
    """
    return (isinstance(obj, a_class))
