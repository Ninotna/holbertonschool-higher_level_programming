#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    inherits_from - returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False
    @obj: the object to check
    @a_class: the class to check inheritance from
    Return: True if obj is an instance of a class that inherited from a_class, else False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
