#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        x = ""
        for c in n:
            print("{:s}{:d}".format(x, c),end="")
            x = " "
        print()
