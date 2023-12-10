#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxNumber = my_list[0]
    for i in my_list:
        j = 1
        if (i < my_list[j]):
            maxNumber = my_list[j]
        j += 1
    return maxNumber
