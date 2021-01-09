#!/usr/bin/python3

""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    count = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(error)

    for x in matrix:

        if type(x) is not list:
            raise TypeError(errortoolong)
        rows.append(len(x))

        for item in x:

            if type(item) not in [int, float]:
                raise TypeError(errortoolong)
            count += 1

    if len(set(rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new = list(map(lambda x:
                   list(map(lambda i: round(i / div, 2), x)), matrix))

    return (new)
