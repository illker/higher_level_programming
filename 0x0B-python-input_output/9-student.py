#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """returns the dictionary"""

    def __init__(first_name, last_name, age):
        """method init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method json dict"""
        return self.__dict__
