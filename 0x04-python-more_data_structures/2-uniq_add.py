#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seto = set(my_list)
    for n in seto:
        total += n
    return total
