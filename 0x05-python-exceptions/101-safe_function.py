#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    func = 0
    try:
        func = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None
    return func
