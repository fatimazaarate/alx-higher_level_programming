#!/usr/bin/python3
"""a class Base that refer to the base class of other classes"""
import json


class Base:
    """A base class for other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """a static method that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON string
        representation of list_objs to a file"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dictionary = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """a static method that returns the list of the
        JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance
        with all attributes already set (using a "dummy")"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """a class method that returns a list of instances"""
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
            if not f:
                return []
            else:
                list = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in list]
