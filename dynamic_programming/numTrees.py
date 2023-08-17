#!/usr/bin/python3
"""LeetCode Problem #96 --> Unique Binary Search Trees"""
from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        for i in range(1, n + 1):
            j = 0
            while j < i:
                dp[i] += dp[j] * dp[i - j - 1]
                j += 1
        return dp[n]
