#!/usr/bin/python3
"""module defnes function that generates
pascal's triangle integer"""


def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    return fact


def pascal_triangle(n):
    """generates intergers for pascal's triangle"""
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(i+1):
            arr[i].append(factorial(i)//(factorial(j)*factorial(i-j)))

    return arr
