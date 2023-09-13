#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    for n in range(len(my_list)):
        if my_list[n] == search:
            new.append(replace)
        else:
            new.append(my_list[n])
    return new
