#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return([list(map(lambda x: x * x, matrix[i]))
            for i in range(0, len(matrix))])
