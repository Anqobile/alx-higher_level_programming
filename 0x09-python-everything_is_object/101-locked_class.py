#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass for 'first name' attributes.
    """

    __slots__ = ["first_name"]
