#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniqlist = set(my_list)
    for i in uniqlist:
        result += i
    return(result)
