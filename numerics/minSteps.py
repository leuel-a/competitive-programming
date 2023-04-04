#!/usr/bin/python3
"""LeetCode Problem #650 --> 2 Keys Keyboard"""


class Solution:
    def minSteps(self, n: int) -> int:
        min_steps = 0

        d = 2
        while n > 1:
            while n % d == 0:
                min_steps += d
                n //= d
            d += 1
        return min_steps
        
