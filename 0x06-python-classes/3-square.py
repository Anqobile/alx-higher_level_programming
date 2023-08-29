#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """square Representation."""

    def __init__(self, size=0):
        """new Square initialization.

        Args:
            size (int): The new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size has be an integer")
        elif size < 0:
            raise ValueError("size has to be >= 0")
        self.__size = size

    def area(self):
        """Return the square current area."""
        return (self.__size * self.__size)

