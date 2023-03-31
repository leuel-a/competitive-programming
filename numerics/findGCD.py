#!/usr/bin/python3
"""LeetCode Problem #1979 --> Find the Greatest Common Divisor of Array"""


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)
        return gcd(max(nums), min(nums))
