#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """list of lists of integers"""
    if n <= 0:
        return l = []

    l = []
    trow = [1]
    y = [0]
    for x in range(n):
        l.append(trow)
        trow = [left+right for left, right in zip(trow+y, y+trow)]
    return l
