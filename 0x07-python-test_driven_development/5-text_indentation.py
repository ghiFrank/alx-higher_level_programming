#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for n in range(0, len(text)):
        if text[n] in ['.', '?', ':']:
            print(text[n], end="\n\n")
        elif text[n] == ' ' and text[n-1] in ['.', '?', ':']:
            continue
        else:
            print(text[n], end="")
