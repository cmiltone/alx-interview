#!/usr/bin/python3
"""modules deaclres a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only
need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """returns True if data is valid UTF-8 or False otherwise"""
    num_arr = len(data)
    _continue = 0

    for i in range(num_arr):
        if _continue > 0:
            _continue -= 1

            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            _continue = 0
        elif data[i] & 0b11111000 == 0b11110000:
            tab = 4

            if num_arr - i >= tab:
                n = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + tab],
                ))

                if not all(n):
                    return False
                _continue = tab - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            tab = 3

            if num_arr - i >= tab:
                n = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + tab],
                ))

                if not all(n):
                    return False

                _continue = tab - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            tab = 2

            if tab <= num_arr - i:
                n = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + tab],
                ))

                if not all(n):
                    return False
                _continue = tab - 1
            else:
                return False
        else:
            return False
    return True
