#!/usr/bin/python3
""" this is where modules go """


def say_my_name(first_name, last_name=""):

    """ this function prints a name """

    if type(first_name) != str:
        TypeError("first_name must be a string")
    elif last_name and type(last_name) != str:
        TypeError("last_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
