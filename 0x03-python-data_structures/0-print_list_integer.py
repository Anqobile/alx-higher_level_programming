#!/usr/bin/python3
def print_list_integer(my_list=[]):

   "print the list of all integers"
   for y in my_list:
       print("{:d}".format(y))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)