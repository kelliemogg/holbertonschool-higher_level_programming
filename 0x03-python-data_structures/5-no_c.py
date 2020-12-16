#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.copy()
    for x in my_string:
        if x == 'c':
            continue
        elif x == 'C':
            continue
        else:
            x += new_string
            return(new_string)
