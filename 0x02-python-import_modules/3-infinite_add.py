#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for n in argv[1:]:
        total += int(n)
    print(total)