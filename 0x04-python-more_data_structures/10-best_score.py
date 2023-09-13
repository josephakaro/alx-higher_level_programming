#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    first = 0
    first_key = ""
    for key, value in a_dictionary.items():
        if value > first:
            first = value
            first_key = key
    return first_key
