#!/usr/bin/python3
""" LockedClass that prevents user from dynamically creating new instance attribut,
    exept if the new instance attribute is called first_name
"""


class LockedClass:
    __slots__ = ['first_name']
    def __init__(self) -> None:
        pass
