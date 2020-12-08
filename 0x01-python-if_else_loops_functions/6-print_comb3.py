#!/usr/bin/python3
for f in range(0, 9):
    for l in range(0, 9):
        if f is not l:
            print("{}{}, ".format(f, l), end="")
        elif (f is 8) and (l is 9):
            print("{}{}".format(f, l))
