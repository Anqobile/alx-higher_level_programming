#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size):
        """Initialization of new square.

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
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
