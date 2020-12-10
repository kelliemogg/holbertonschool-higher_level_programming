#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in range(0, len(argv)):
        if len(argv) is 1:
            print("0 arguments.")
        elif len(argv) is 2:
            print("1 argument:\n1: {}".format(argv[1:]))
            break:
        else:
            print("{} arguments:".format(len(argv) - 1), end="")
            print("\n{}: {}".format(i + 1, argv[1:]))
