#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda s: replace if s == search else s, my_list))
    return (new_list)
