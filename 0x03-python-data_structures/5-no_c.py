#!/usr/bin/python3
def no_c(my_string):
    newS = ""
    for n in my_string:
        if n != 'c' and n != 'C':
            newS += n
    return newS
