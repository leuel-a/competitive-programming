#!/usr/bin/python3
"""LeetCode Problem #1137 --> N-th Tribonacci Number"""
from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def dp(i: int) -> int:
            if i not in memo:
                memo[i] = dp(i - 3) + dp(i - 2) + dp(i - 1)
            return memo[i]
        return dp(n)
