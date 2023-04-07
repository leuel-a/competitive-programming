#!/usr/bin/python3
"""LeetCode Problem #2373 --> Largest Local Variables in a Matrix"""


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        def maxFinder(row_idx: int, col_idx: int) -> int:
            _max = float('-inf')
            for i in range(row_idx, row_idx + 3):
                for j in range(col_idx, col_idx + 3):
                    _max = max(_max, grid[i][j])
            return _max

        maxLocal = [[0] * (len(grid) - 2) for i in range(len(grid) - 2)]
        for i in range(len(maxLocal)):
            for j in range(len(maxLocal[i])):
                maxLocal[i][j] = maxFinder(i, j)
        return maxLocal

