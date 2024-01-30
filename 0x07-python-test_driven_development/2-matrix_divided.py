#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrixo = []
    for n in range(len(matrix)):
        if not isinstance(matrix[n], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        matrixo.append([])
        for i in range(len(matrix[n])):
            if not isinstance(matrix[n][i], (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            lengtho = len(matrix[0])
            if len(matrix[n]) != lengtho:
                raise TypeError(
                    "Each row of the matrix must have the same size")

            matrixo[n].append(round((matrix[n][i] / div), 2))

    return matrixo
