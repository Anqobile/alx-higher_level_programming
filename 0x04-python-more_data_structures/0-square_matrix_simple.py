#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrixcopy()

    for s_m_s in range(len(matrix)):
        new_matrix[s_m_s] = list(map(lambda x: x**2, matrix[s_m_s]))

    return (new_matrix)
