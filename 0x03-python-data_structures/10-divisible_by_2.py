#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    newL = []
    for n in my_list:
        if n % 2 == 0:
            newL.append(True)
        else:
            newL.append(False)
    return newL
