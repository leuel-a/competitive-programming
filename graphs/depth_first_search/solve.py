#!/usr/bin/python3
"""LeetCode Problem #130 --> Surrounded Regions"""
from typing import List



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def depth_first_search(row: int, col: int) -> bool:
            visited.add((row, col))
            # print(visited)

            for row_inc, col_inc in directions:
                new_row = row + row_inc
                new_col = col + col_inc

                if not in_bound(new_row, new_col):
                    return False

                if (new_row, new_col) not in visited and board[new_row][new_col] == 'O':
                    if not depth_first_search(new_row, new_col):
                        return False
            return True

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 'X':
                    visited.clear()
                    if not depth_first_search(i, j):
                        continue
                    for row, col in visited:
                        board[row][col] = 'X'
