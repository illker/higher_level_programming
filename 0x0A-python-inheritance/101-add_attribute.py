#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attribute, value):
    """adds a new attribute"""

    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
