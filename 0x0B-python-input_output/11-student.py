#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """returns the dictionary"""

    def __init__(self, first_name, last_name, age):
        """method init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method json dict"""
        if attrs is None:
            return (self.__dict__)
        else:
            n = {}
            for a in attrs:
                if hasattr(self, a):
                    n[a] = getattr(self, a)
            return (n)

    def reload_from_json(self, json):
        """method reload json"""
        if json is not None:
            self.__dict__ = json
