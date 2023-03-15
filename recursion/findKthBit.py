#!/usr/bin/python3
"""LeetCode #1545 --> Find Kth Bit in Nth Binary String"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def findBinaryString(n: int) -> str:
            if n == 1:
                return '0'
            val = findBinaryString(n - 1)
            return val + '1' + ''.join('1' if x == '0' else '0' for x in val)[::-1]
        return findBinaryString(n)[k - 1]
