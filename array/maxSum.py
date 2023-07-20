#!/usr/bin/python3
"""LeetCode Problem #2428 --> Maximum Sum of an Hourglass"""
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = float('-inf')

        for i in range(len(grid)):
            if i + 2 >= len(grid):
                continue
            for j in range(len(grid[i])):
                if j + 2 >= len(grid[i]):
                    break

                curr = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]\
                    + grid[i + 1][j + 1] + grid[i + 2][j] + grid[i + 2][j + 1]\
                    + grid[i + 2][j + 2]
                max_sum = max(max_sum, curr)
        return max_sum
