#!/usr/bin/python3
"""LeetCode Problem #542 --> 01 Matrix"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue, visited = deque(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        while queue:
            row, col, dist = queue.popleft()
            for row_inc, col_inc in directions:
                new_row, new_col = row + row_inc, col + col_inc

                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    mat[new_row][new_col] = dist + 1
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))
        return mat
