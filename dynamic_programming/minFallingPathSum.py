#!/usr/bin/python3
"""LeetCode Problem #931 --> Minimum Falling Path Sum"""
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [0 for _ in range(n)]

        for i in range(n):
            curr = [float('inf') for _ in range(n)]

            for col in range(n):
                curr[col] = matrix[i][col] + prev[col]

                if col - 1 >= 0:
                    curr[col] = min(curr[col], matrix[i][col] + prev[col - 1])
                if col + 1 < n:
                    curr[col] = min(curr[col], matrix[i][col] + prev[col + 1])
            prev = curr
        return min(curr)
