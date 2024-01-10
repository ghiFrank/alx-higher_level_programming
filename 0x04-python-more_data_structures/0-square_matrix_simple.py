#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = []
    for n in range(len(matrix)):
        newM.append([])
        for i in range(len(matrix[n])):
            newM[n].append(matrix[n][i] * matrix[n][i])
    return newM
