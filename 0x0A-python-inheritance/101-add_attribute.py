#!/usr/bin/python3
""" add a new attribute to an obj if possible """


def add_attribute(obj, name, value):
    """ check if obj can have new attribute """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
