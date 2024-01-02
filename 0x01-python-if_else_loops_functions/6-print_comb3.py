#!/usr/bin/python3
for x in range(0, 10):
    for n in range(x + 1, 10):
        if x == 8 and n == 9:
            print("{}{}".format(x, n), end='\n')
            continue
        print("{}{}".format(x, n), end=', ')
