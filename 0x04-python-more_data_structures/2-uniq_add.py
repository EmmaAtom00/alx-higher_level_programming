#!/usr/bin/python3

def uniq_add(my_list=[]):
    j = 0
    existed_list = []
    for i in my_list:
        if (i not in existed_list):
            existed_list.append(i)
            j += i
    return j
