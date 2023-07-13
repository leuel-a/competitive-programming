#!/usr/bin/python3
"""LeetCode Problem #934 --> Shortest Bridge"""
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        groups = [set(), set()]
        queue = deque()

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def get_neighbours(row: int, col: int) -> List[int]:
            """Function that accepts a row and a column and returns
            all valid neighbours
            """
            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]

            neighbours = []
            for r_inc, c_inc in directions:
                new_row = row + r_inc
                new_col = col + c_inc

                if inbound(new_row, new_col):
                    neighbours.append((new_row, new_col))
            return neighbours

        # Group Creation Part
        for group in groups:
            flag = False
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    val = grid[i][j]
                    if val == 1 and (i, j) not in groups[0] and (i, j) not in groups[1]:
                        flag = True
                        queue.append((i, j))
                        group.add((i, j))

                        while queue:
                            row, col = queue.popleft()

                            for a, b in get_neighbours(row, col):
                                if (a, b) not in group and grid[a][b] == 1:
                                    group.add((a, b))
                                    queue.append((a, b))
                        break
                if flag:
                    flag = False
                    break

        # Main Solution Part
        visited = set()
        for val in groups[0]:
            queue.append((val, 0))
            visited.add(val)

        while queue:
            (row, col), flips = queue.popleft()
            if (row, col) in groups[1]:
                return flips

            for new_row, new_col in get_neighbours(row, col):
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), flips + 1 if grid[new_row][new_col] == 0 else flips))
