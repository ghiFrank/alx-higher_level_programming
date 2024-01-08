#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (0, None)
    return (sorted(my_list)[-1])
