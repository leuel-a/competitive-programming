#!/usr/bin/python3
"""LeetCode Problem #914 --> X of a Kind in a Deck of Cards"""
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        frequency = Counter(deck)
        _min = min(frequency.values())

        while _min > 1:
            for val in frequency.values():
                if val % _min != 0:
                    _min -= 1
                    break
            else:
                return True
        return False
