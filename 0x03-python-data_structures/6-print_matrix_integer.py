#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        x = ""
        for c in n:
            print("{:d}".format(c).end="")
            x = " "
        print()
