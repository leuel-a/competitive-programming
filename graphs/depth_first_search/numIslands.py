"""Leetcode Problem #200 --> Number of Islands"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < m

        def dfs(row: int, col: int):
            visited.add((row, col))

            for rInc, cInc in directions:
                newR = row + rInc
                newC = col + cInc

                if inbound(newR, newC) and (newR, newC) not in visited and grid[newR][newC] == "1":
                    dfs(newR, newC)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count
