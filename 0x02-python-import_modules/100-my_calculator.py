#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    o = str(argv[2])
    b = int(argv[3])
    opera = ['+', '-', '*', '/']
    if o == opera[0]:
        print("{} {} {} = {}".format(a, o, b, add(a, b)))
    elif o == opera[1]:
        print("{} {} {} = {}".format(a, o, b, sub(a, b)))
    elif o == opera[2]:
        print("{} {} {} = {}".format(a, o, b, mul(a, b)))
    elif o == opera[3]:
        print("{} {} {} = {}".format(a, o, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)