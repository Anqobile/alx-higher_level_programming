#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Representation of a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize the new Rectangle.
            height: The new rectangle's height.
            width: The rectangle's width.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Set/get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not  int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
