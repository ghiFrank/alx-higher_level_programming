#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
        return num_chars_written
