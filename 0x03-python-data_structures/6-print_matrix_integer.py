#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in n:
            endo = "" if i == len(n) else " "
            print('{:d}'.format(i), end = endo)
        print('\n')
