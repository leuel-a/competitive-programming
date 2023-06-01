#!/usr/bin/python3
"""LeetCode Problem #62 --> Unique Paths"""
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def dp(row: int, col: int) -> int:
            if (row, col) == (m - 1, n - 1):
                return 1

            if (row, col) in memo:
                return memo[(row, col)]


            ways = 0
            if in_bound(row, col + 1):
                ways += dp(row, col + 1)

            if in_bound(row + 1, col):
                ways += dp(row + 1, col)
            memo[(row, col)] = ways
            return memo[(row, col)]
        return dp(0, 0)
