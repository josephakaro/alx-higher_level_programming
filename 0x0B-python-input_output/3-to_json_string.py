#!/usr/bin/python3
""" module """


def to_json_string(my_obj):
    """ return func that writes an obj to a text file """
    import json
    return json.dumps(my_obj, ensure_ascii=False)
