#!/usr/bin/python3
"""LeetCode Problem #1091 --> Shortest Path in Binary Matrix"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid)

        if grid[0][0] == 0:
            if n == 1:
                return 1
            queue.append((0, 0, 1))
            grid[0][0] = 1

        while queue:
            row, col, dist = queue.popleft()
            for row_inc, col_inc in directions:
                new_row, new_col = row_inc + row, col_inc + col
                if in_bound(new_row, new_col) and grid[new_row][new_col] == 0:
                    if new_row == new_col == n - 1:
                        return dist + 1
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, dist + 1))
        return -1
