#!/usr/bin/python3
"""LeetCode Problem #1823 --> Find the Winner of the Circular Game"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        losers = {}

        def loserInRound(start: int) -> int:
            if len(losers) == len(friends) - 1:
                return friends[start]

            _count, prev, idx = 0, 0, start
            while _count != k:
                if friends[idx] not in losers:
                    _count += 1
                    prev  = idx
                idx = (idx + 1) % len(friends)
            losers[friends[prev]] = False

            while friends[idx] in losers:
                idx = (idx + 1) % len(friends)
            return loserInRound(idx)
        return loserInRound(0)
