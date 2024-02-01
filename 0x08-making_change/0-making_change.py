#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of
coin in the list
Your solution's runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """gets the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    diff = total
    return_val = 0
    index = 0
    arr = sorted(coins, reverse=True)
    n = len(coins)
    while diff > 0:
        if index >= n:
            return -1
        if diff - arr[index] >= 0:
            diff -= arr[index]
            return_val += 1
        else:
            index += 1
    return return_val
