#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for n in my_string:
        if n != "C" and n != "c":
            new = new + n
