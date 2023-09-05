#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        divi = a / b
    except (TypeError, ZeroDivisionError):
        divi = None
    finally:
        print("Inside result: {}".format(divi))
    return (divi)

