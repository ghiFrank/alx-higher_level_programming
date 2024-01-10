#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = []
    for n in my_list:
        if n == search:
            newl.append(replace)
            continue
        newl.append(n)
    return newl
