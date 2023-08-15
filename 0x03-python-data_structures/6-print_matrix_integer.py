#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for i in m:
            print("{:d}".format(i), end =" ")
            if i != m[-1]:
                print(end=" ")
            print ()
