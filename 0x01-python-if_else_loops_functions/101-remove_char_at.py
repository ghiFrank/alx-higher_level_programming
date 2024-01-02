#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = list(str)
    if n >= 0 and n < len(str):
        str2.remove(str[n])
    str2 = ''.join(str2)
    return (str2)
