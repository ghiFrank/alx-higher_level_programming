#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for n in range(0, x):
            print(my_list[n], end="")
            total += 1
    except IndexError:
        None
    print()
    return total
