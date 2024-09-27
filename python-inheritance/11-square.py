#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
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

    def area(self):
        """
        Returns the area of the rectangle.

        Return: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        [Rectangle] <width>/<height>

        Return: A formatted string representing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class to represent a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the size of the square after validation using integer_validator.

        @arg size: The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.

        Return: The area (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square in the format:
        [Square] <size>/<size>

        Return: A formatted string representing the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
