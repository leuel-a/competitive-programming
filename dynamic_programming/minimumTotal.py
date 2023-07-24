#!/usr/bin/python3
"""LeetCode Problem #120 --> Triangle"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(dp) and 0 <= col < len(dp)

        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[i]), -1, -1):
                if j > len(triangle[i]) - 1:
                    continue

                a = dp[i + 1][j] if in_bound(i + 1, j) else 0
                b = dp[i + 1][j + 1] if in_bound(i + 1, j + 1) else 0

                dp[i][j] = triangle[i][j] + min(a, b)
        return dp[0][0]
