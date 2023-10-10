"""Leetcode Problem #994 --> Rotting Oranges"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        minutes = 0
        while queue:
            row, col, count = queue.popleft()
            minutes = max(minutes, count)

            for rInc, cInc in directions:
                newR, newC = row + rInc, col + cInc

                if inbound(newR, newC) and grid[newR][newC] == 1:
                    grid[newR][newC] = 2
                    queue.append((newR, newC, count + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes
