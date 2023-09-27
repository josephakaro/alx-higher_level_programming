#!/usr/bin/python3
def safe_print_division(a, b):
    divider = None
    try:
        divider = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(divider))
    return divider
