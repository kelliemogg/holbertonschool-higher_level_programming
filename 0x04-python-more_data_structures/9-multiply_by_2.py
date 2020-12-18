#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    total = 0
    new_dict = a_dictionary.copy()
#    for key in new_dict:
#        count = new_dict[key]
#        total += count
        for key in new_dict:
            new_dict[key] = (new_dict[key] * 2)
        return(new_dict)
