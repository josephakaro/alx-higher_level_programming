""" LockedClass that prevents user from dynamically creating new instance attribut,
    exept if the new instance attribute is called first_name
"""

@classmethod
class LockedClass:
    if not isinstance(LockedClass, first_name):
        raise AttributeError("")
    else:
        def __init__(self) -> None:
            pass