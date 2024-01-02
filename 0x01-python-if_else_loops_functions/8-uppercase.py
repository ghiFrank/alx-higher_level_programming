#!/usr/bin/python3
def uppercase(str):
    for x in str:
        formatted_x = chr(ord(x) - 32) if 97 <= ord(x) <= 122 else x
        print("{}".format(formatted_x), end='')
    print()
