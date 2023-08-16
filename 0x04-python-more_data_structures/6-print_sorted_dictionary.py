#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    def_pnt = list(a_dictionary.keys())
    def_pnt.sort()
    for d in def_pnt:
        print("{}: {}".format(d, a_dictionary.get(d)))
