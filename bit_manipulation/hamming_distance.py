#!/usr/bin/python3
"""LeetCode Problem #461 --> Hamming Distance"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_dist = 0

        for i in range(max(x.bit_length(), y.bit_length())):
            if x & (1 << i) != y & (1 << i):
                hamming_dist += 1
        return hamming_dist
