#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except:
        if a | b is 0:
            print("Inside result: None")
    finally:
        print("Inside result: {}".format(res))
