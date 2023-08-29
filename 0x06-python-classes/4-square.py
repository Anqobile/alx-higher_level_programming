#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """square representation."""

    def __init__(self, size=0):
        """new square Initialization.

        Args:
            size (int): The new square size.
        """
        self.size = size

    @property
    def size(self):
        """Set/get the square current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size has to be an integer")
        elif value < 0:
            raise ValueError("size has to be >= 0")
        self.__size = value

    def area(self):
        """Return the of the square current area."""
        return (self.__size * self.__size)
