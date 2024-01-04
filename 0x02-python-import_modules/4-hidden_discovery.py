#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    files = dir()
    for n in range(0, len(files)):
        if files[n][:2] != "__":
            print("{:s}".format(files[n]))