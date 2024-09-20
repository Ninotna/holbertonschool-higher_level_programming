#!/usr/bin/python3
"""
8-rectangle.py

This module initializes a class called Rectangle.
"""


class Rectangle:
    """
    The 'Rectangle' class represents a generic rectangle.

    Attributes:
        __width (int): The width of a rectangle.
        __height (int): the height of a rectangle.
        number_of_instances (int): The number of instances of the class.
        print_symbol (char): The symbole used to prints the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize private instance attributes: 'width' and 'height'.

        Args:
            width (int): The width of a rectangle.
            height (int): The height of a rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Check exception type and value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Check exception type and value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method: def perimeter(self):
        that returns the current rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle
        with the character defined by print_symbol
        """
        rectangle_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for line in range(self.__height):
            for index in range(self.__width):
                rectangle_string += str(self.print_symbol)
            rectangle_string += "\n"

        return rectangle_string[:-1]  # Remove the last newline character

    def __repr__(self):
        """
        Return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area

        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle

        Raises:
            TypeError: if a rectangle is not an instance of class Rectangle

        Returns:
            The biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2