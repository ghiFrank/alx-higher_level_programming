#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newD = a_dictionary.copy()
    for n in a_dictionary:
        newD[n] *= 2
    return newD
