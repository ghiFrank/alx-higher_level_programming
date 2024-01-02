#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        strn = str(number)
        print('{}'.format(strn[-1]), end='')
        return strn[-1]
