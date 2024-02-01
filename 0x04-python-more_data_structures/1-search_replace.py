#!/usr/bin/python3

def search_replace(my_list, search, replace):
    j = 0
    new_list = []
    for i in my_list:
        new_list.append(i)
        if (i == search):
            new_list[j] = replace
        j += 1
    return new_list
