#!/usr/bin/python3
"""Only sub class"""


def inherits_from(obj, a_class):
    """object is an instance"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
