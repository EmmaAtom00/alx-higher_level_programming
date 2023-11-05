#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    my_listN = my_list.copy()

    if (idx < 0 or idx >= len(my_list)):
        return my_listN
    else:
        my_listN[idx] = element
        return my_listN
