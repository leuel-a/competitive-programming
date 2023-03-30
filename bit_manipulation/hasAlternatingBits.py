#!/usr/bin/python3
"""LeetCode Problem #693 --> Binary Number with Alternating Bits"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        for i in range(1, n.bit_length()):
            if (n & (1 << i) != 0) and (n & (1 << (i - 1)) != 0) or (n & (1 << i) == 0) and (n & (1 << (i - 1)) == 0):
                return False
        return True
