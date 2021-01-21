#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """representing the Pascals"""
    if n <= 0:
        return []

    l = []
    trow = [1]
    y = [0]
    for x in range(n):
        l.append(trow)
        trow = [left + right for left, right in zip(trow + y, y + trow)]
    return l
