#!/usr/bin/python3
"""module defnes function that generates
pascal's triangle integer"""


def pascal_triangle(n):
    """generates intergers for pascal's triangle"""
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(i+1):
            arr[i].append(0)

    return arr
