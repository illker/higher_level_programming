#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic1 = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            dic1.append(key)
    for key in dic1:
        del a_dictionary[key]
    return a_dictionary
