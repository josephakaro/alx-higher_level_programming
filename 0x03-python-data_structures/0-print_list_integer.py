#!/usr/bin/python3
"""
    Python List: print list of integers
"""
def print_list_integer(my_list=[]):
    for n in my_list:
        fmt = "{:d}".format(n)
        print(fmt)
