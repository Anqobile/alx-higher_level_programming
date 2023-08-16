#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = list(a_dictionary.keys())

    for cd in delete_keys:
        if value == a_dictionary.get(cd):
            del a_dictionary[cd]

    return (a_dictionary)
