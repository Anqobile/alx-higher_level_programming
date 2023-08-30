#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to be divided.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for h in range(0, list_length):
        try:
            divi = my_list_1[h] / my_list_2[h]
        except TypeError:
            print("wrong type")
            divi = 0
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        except IndexError:
            print("out of range")
            divi = 0
        finally:
            new_list.append(divi)
    return (new_list)
