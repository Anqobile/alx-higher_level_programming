#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of of my_list to print elements.

    Returns:
        The number of printed elements.
    """
    rey = 0
    for h in range(x):
        try:
            print("{}".format(my_list[h]), end="")
            rey += 1
        except IndexError:
            break
    print("")
    return (rey)

