#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    num = 0
    dictio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for e, n in enumerate(roman_string):
        if n is not roman_string[0]:
            if roman_string[e - 1] == 'I' and (n == 'V' or n == 'X'):
                num = num + dictio[n] - 2
                continue
            if roman_string[e - 1] == 'X' and (n == 'L' or n == 'C'):
                num = num + dictio[n] - 20
                continue
            if roman_string[e - 1] == 'C' and (n == 'D' or n == 'M'):
                num = num + dictio[n] - 200
                continue
        num += dictio[n]
    return num
