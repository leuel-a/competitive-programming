#!/usr/bin/python3
"""LeetCode Problem #695 --> Max Area of Islands"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def depth_first_search(row: int, col: int) -> int:
            if (row, col) in visited:
                return 0

            val = 1
            visited.add((row, col))
            for row_inc, col_inc in directions:
                new_row = row + row_inc
                new_col = col + col_inc

                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    val += depth_first_search(new_row, new_col)
            return val

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, depth_first_search(i, j))

        return max_area
