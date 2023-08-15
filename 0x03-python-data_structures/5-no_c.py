#!/usr/bin/env python3
def no_c(my_string):
    no_c = [b for b in my_string if b != 'c' and b != 'C']
    return ("".join(no_c))
