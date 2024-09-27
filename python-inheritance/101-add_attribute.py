#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object if possible.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    @arg obj: The object to which the attribute is added.
    @arg attribute: The name of the attribute to add.
    @arg value: The value of the attribute to add.
    Return: None, raises TypeError if the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
