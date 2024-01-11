#!/usr/bin/python3
""" modules implements a arr to n queens problem"""
import sys


arrs = []
n = 0
pos = None


def parse_args():
    """gets args"""
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(p0, p1):
    """returns True if the positions of two queens are in an attacking mode, or False otherwise"""
    if (p0[0] == p1[0]) or (p0[1] == p1[1]):
        return True
    return abs(p0[0] - p1[0]) == abs(p0[1] - p1[1])


def col_exists(col):
    """returns True if a col exists in arrs, or False otherwise"""
    global arrs
    for stn in arrs:
        i = 0
        for stn_pos in stn:
            for grp_pos in col:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_arr(row, col):
    """gets n queens problem array"""
    global arrs
    global n
    if row == n:
        current_col = col.copy()
        if not col_exists(current_col):
            arrs.append(current_col)
    else:
        for l in range(n):
            a = (row * n) + l
            exists = zip(list([pos[a]]) * len(col), col)
            k = map(lambda x: is_attacking(x[0], x[1]), exists)
            col.append(pos[a].copy())
            if not any(k):
                build_arr(row + 1, col)
            col.pop(len(col) - 1)


def get_arrs():
    """get solutions"""
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    col = []
    build_arr(a, col)


n = parse_args()
get_arrs()
for arr in arrs:
    print(arr)