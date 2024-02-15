#!/usr/bin/python3
"""module declares a function determine the winner of a prime game
"""


def isWinner(x, nums):
    """returns the winner of prime game with X rounds"""
    if x < 1 or not nums:
        return None
    maria_count = 0
    ben_count = 0
    n = max(nums)
    rounds = [True for _ in range(1, n + 1, 1)]
    rounds[0] = False
    for i, is_prime in enumerate(rounds, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            rounds[j - 1] = False
    for _, n in zip(range(x), nums):
        count = len(list(filter(lambda x: x, rounds[0: n])))
        ben_count += count % 2 == 0
        maria_count += count % 2 == 1
    if maria_count == ben_count:
        return None
    return 'Maria' if maria_count > ben_count else 'Ben'
