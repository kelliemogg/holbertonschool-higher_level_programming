#!/usr/bin/python3
for f in range(0, 10):
    for l in range(0, 10):
        if f is not l and f is not 8:
            if l - f <= 0:
                continue
            else:
                print("{}{}, ".format(f, l), end="")
        elif (f is 8) and (l is 9):
            print("{}{}".format(f, l))
