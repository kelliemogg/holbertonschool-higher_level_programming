#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) is 1:
        print("0 arguments.")
    elif len(argv) is 2:
        for position, arg in enumerate(argv[1:]):
            print("1 argument:\n1: {}".format(arg))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for position, arg in enumerate(argv[1:]):
            print("{}: {}".format(position + 1, arg))
