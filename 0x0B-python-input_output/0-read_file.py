#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
