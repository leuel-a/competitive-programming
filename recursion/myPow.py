#!/usr/bin/python3
"""Defines the Solution Class"""


class Solution:
    """Defines the Solution class for LeetCode Problem #50"""
    def myPow(self, x: float, n: int) -> float:
        """Returns x raised to n"""
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1 / x
        if n % 2 != 0:
            return x * self.myPow(x * x, n // 2)
        return self.myPow(x * x, n // 2)

