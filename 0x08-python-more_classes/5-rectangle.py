#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.
            width: The new rectangle's width.
            height: The new rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/get the Rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width has to be an integer")
        if value < 0:
            raise ValueError("width has to be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the Rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height has to be an integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value

    def area(self):
        """Return the Rectangle's area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the Rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for h in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
