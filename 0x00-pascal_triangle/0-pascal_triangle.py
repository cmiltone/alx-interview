#!/usr/bin/python3
"""module defnes function that generates
pascal's triangle integer"""
from math import factorial


def pascal_triangle(n):
    """generates intergers for pascal's triangle"""

    arr = []
    for i in range(n):
        arr.append([])
        for j in range(i+1):
            arr[i].append(factorial(i)//(factorial(j)*factorial(i-j)))

    return arr
