#!/usr/bin/python3
def max_integer(my_list=[]):
      if len(my_list) == 0:
        return None
    
    mi = my_list[0]
    for b in range(len(my_list)):
        if mi < my_list[b]:
            mi = my_list[b]

            return mi

