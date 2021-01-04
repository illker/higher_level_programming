#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        z = a / b
    except ZeroDivisionError:
        z = None
    finally:
        print("Inside result: {}".format(z))
        return z
