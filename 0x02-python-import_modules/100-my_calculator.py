#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
from add_0 import add
operator = {"+", "-", "*", "/"}
args = len(argv)
a = int(argv[1])
b = int(argv[3])
result = add(a, b)

if args != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif args == 4:
    for i in operator:
        if argv[2] != {"+", "-", "*", "/"}:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            print("{} {} {} = {}".format(a, operator, b, result))
