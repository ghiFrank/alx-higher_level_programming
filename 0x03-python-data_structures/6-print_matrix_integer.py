#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for n in matrix:
        if len(n) == 0:
            print()
        for i in range(len(n)):
            print('{:d}'.format(n[i]), 
                  end = "\n" if i is len(n) - 1 else " ")
