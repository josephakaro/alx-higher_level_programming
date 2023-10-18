#!/usr/bin/python3
"""
    This module holds Base Class of all Classes in this project files.\
    It is aimed at managing id attributes of all future classes and avoid at duplicating same code.
"""
import json

class Base:
    """ Base class """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ Initilizier function with private attributes and id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries, default=str)
            return json_string

    @staticmethod
    def from_json_string(json_string):
        """ returns a list from the json string """
        a = []
        if json_string is None or len(json_string) == 0:
            return a
        else:
            json_obj = json.loads(json_string)
            return json_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep to a file """
        cls_name = cls.__name__ + ".json"
        list_dict = []

        if list_objs is None:
            list_objs = []

        for item in list_objs:
            list_dict.append(item.to_dictionary())

        with open(cls_name, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance from set values """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        list_obj = []

        if not cls.__name__ + ".json":
            return list_obj
        else:
            with open(cls.__name__ + ".json", mode="r") as f:
                """ open and read the file """
                for object in cls.from_json_string(f.read()):
                    list_obj.append(cls.create(**object))
            return list_obj
