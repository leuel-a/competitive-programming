"""Leetcode Problem #62 --> Unique Paths"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a, b = m - 1, n - 1

        # The total number of ways to go down --> a
        # The total number of ways to go right --> b

        # Then the answer will be in how many distnict ways can I arrange these directions --> (a + b)! / (a! * b!)

        return int(math.factorial(a + b) / (math.factorial(a) * math.factorial(b)))
