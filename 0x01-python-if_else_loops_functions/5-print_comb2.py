#!/usr/bin/python3
for c in range(0, 100):
    if c < 10:
        print("0{}, ".format(c), end="")
    elif c > 9 and c < 99:
        print("{}, ".format(c), end="")
    elif c == 99:
        print("{}".format(c))
