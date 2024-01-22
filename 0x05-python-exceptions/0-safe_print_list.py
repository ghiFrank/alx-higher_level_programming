#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    try:
        total = 0
        for n in range(0,x):
            print(my_list[n], end="")
            total += 1
        print("\n")
        return total
    except:
        return total
