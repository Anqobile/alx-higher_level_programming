#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square representation"""

    def __init__(body, size):
        """New Square initialization.

        Args:
            size (int): The size of the new square.
        """
        body.__size = size
