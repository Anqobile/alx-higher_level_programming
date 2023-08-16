#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [sms[:] for sms in matric]
    for sm, sms in enumerate(new_matrix):
        for sm2, col in enumerate(new_matrix):
            new_matrix[sm][sm2] = sms[sm2] ** 2
            return (new_matrix)
