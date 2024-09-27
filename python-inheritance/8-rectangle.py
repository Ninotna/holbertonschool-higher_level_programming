#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
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


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes width and height after validation using integer_validator.

        @arg width: The width of the rectangle.
        @arg height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
