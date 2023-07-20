#!/usr/bin/python3
"""LeetCode Problem #1926 --> Nearest Exit from Entrance in Maze"""
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        visited.add((entrance[0], entrance[1]))
        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            row, col, dist = queue.popleft()

            for row_c, col_c in directions:
                new_row = row + row_c
                new_col = col + col_c

                if not in_bound(new_row, new_col) and dist > 0:
                    return dist

                if in_bound(new_row, new_col) and maze[new_row][new_col] != '+' and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))
        return -1
