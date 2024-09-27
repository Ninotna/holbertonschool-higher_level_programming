#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""

class BaseGeometry:
    """
    A class to represent BaseGeometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        @arg name: The name of the parameter (assumed to be a string).
        @arg value: The value to validate (expected to be an integer).
        Return: None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
