#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Representation of a circle."""

    def __init__(self, radius=0):
        """Initialization of a MagicClass.

        Arg:
            radius (float or int): The new MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius has to be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pii)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pii * self.__radius)
