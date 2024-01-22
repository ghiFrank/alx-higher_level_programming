#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    try: 
        while total is not x:
            print(my_list[total], end="")
            total += 1
    except IndexError:
        None
    print()
    return total
