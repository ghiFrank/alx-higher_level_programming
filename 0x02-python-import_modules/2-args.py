#!/usr/bin/python3
from sys import argv
argument = "argument" if len(argv) == 2 else "arguments"
end = "." if len(argv) == 1 else ":"
print("{} {}{}".format(len(argv) - 1, argument, end))
if len(argv) > 1:
    for n,arg in enumerate(argv[1:],1):
        print("{}: {}".format(n, arg))