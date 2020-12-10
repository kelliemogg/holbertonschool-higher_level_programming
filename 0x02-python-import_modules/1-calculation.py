#!/usr/bin/python3
if __name__ == "__main__":

    a = 10
    b = 5

    from calculator_1 import add
    add = add(a, b)
    print("{} + {} = {}".format(a, b, add))

    from calculator_1 import sub
    sub = sub(a, b)
    print("{} - {} = {}".format(a, b, sub))

    from calculator_1 import mul
    mul = mul(a, b)
    print("{} * {} = {}".format(a, b, mul))

    from calculator_1 import div
    div = div(a, b)
    print("{} / {} = {}".format(a, b, div))
