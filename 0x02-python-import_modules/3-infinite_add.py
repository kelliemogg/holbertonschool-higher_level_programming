#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    my_sum = 0
    num = len(argv)

    if num > 2:
        for i in range(1, num):
            argv[i] = int(argv[i])
            my_sum += argv[i]
        print(my_sum)
