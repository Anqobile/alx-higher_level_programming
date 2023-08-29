#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """square representation."""

    def __init__(body, size=0):
        """new Square initialization.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size is an integer")
        elif size < 0:
            raise ValueError("size has to be >= 0")
        body.__size = size
