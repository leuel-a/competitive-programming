#!/usr/bin/python3
"""LeetCode Problem #1905 --> Count Sub Islands"""


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def check_if_valid_sub_island(row: int, col: int) -> bool:
            nonlocal invalid_path_found
            visited.add((row, col))

            for row_inc, col_inc in directions:
                new_row = row + row_inc
                new_col = col + col_inc

                if in_bound(new_row, new_col) and grid2[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    if grid1[new_row][new_col] == 0:
                        invalid_path_found = True
                    check_if_valid_sub_island(new_row, new_col)
            return True

        visited, count = set(), 0
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                invalid_path_found = False
                if grid1[i][j] == 1 and grid2[i][j] == 1 and (i, j) not in visited:
                    check_if_valid_sub_island(i, j)
                    if not invalid_path_found:
                        count += 1
        return count
