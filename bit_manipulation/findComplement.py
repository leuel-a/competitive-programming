#!/usr/bin/python3
"""LeetCode Problem #476 --> Number Complement"""


class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(num.bit_length()):
            num ^= 1 << i
        return num
