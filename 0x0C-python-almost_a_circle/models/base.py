#!/usr/bin/python3
"""Base class"""
import json
import os


class Base():
    """first class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method init"""

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON data representation"""

        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation to file"""

        burger = cls.__name__ + ".json"
        bacon = []
        if list_objs is not None:
            for pepper in list_objs:
                bacon.append(cls.to_dictionary(pepper))
        with open(burger, "w") as pizza:
            pizza.write(cls.to_json_string(bacon))


    @staticmethod
    def from_json_string(json_string):
        """list of the JSON string representation"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes"""

        if cls.__name__ is "Rectangle":
            burger = cls(1, 1)
        elif cls.__name__ == "Square":
            burger = cls(1)
        burger.update(**dictionary)
        return burger

    @classmethod
    def load_from_file(cls):
        """list of instances"""

        tomato = []
        cheese = cls.__name__ + ".json"
        if not os.path.isfile(cheese):
            return tomato
        with open(cheese, mode="r", encoding="utf-8") as meat:
            burger = cls.from_json_string(f.read())
            for add in burger:
                burger_cheese.append(cls.create(**add))
            return burger_cheese
