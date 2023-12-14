
"""
n a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """function to determine minimum number of operations"""
    if not isinstance(n, int):
        return 0
    space = 0
    limit = 1
    total_operations = 0

    while limit < n:
        if space == 0:
            total_operations += 2
            space = limit
            limit += space
        elif n - limit > 0 and (n - limit) % limit == 0:
            total_operations += 2
            space = limit
            limit += space
        elif space > 0:
            total_operations += 1
            limit += space
    return total_operations
