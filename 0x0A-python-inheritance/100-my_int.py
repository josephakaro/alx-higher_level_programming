#!/usr/bin/python3
""" This is no longer an empty class """


class MyInt(int):
    """ reverse equals and not equals """

    def __eq__(self, other):
        """ reverse equals """
        return super().__ne__(other)

    def __ne__(self, other):
        """ reverse not equals """
        return super().__eq__(other)
