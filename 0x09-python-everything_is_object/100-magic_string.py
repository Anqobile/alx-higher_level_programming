#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 1) + 2
    return ("BestSchool, " * (magic_string.n - 2) + "BestSchool")
