#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = ord(c)
        if a > 96 and a < 123:
            a -= 32
        a = chr(a)
        print("{}".format(a), end="")
    print("")
