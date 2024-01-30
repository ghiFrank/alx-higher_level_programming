#!/usr/bin/python3

def copy_list(l):
    newL = []
    return sum([newL + [x] for x in l], [])
