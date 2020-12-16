#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if idx < 0:
            return(None)
        elif idx > my_list[x]:
            return(None)
        else:
            return(idx)
