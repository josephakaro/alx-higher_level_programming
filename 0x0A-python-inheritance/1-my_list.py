#!/usr/bin/python3
""" class MyList will inherit from list """


class MyList(list):
    """ List contains elements of type int """

    def print_sorted(self):
        """ Prints the list in ascending order """
        print(sorted(self))
