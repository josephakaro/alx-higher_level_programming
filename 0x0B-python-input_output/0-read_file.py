#!/usr/bin/python3
""" function to print text to stdout """


def read_file(filename=""):
    """ opens file and sends to stdout """
    with open(filename) as file:
        print(file.read(), end="")
