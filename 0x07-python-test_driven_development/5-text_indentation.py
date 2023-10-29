#!/usr/bin/python3
""" function that adds 2 integers """


def text_indentation(text):
    """ function that prints 2 new lines """

    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    for a in range(len(text)):
        for b in range(len(text)):
            if b == size - 1:
                print("#")
            else:
                print("", end="")
