#!/usr/bin/python3
"""LeetCode Problem #74 --> Search a 2D Matrix"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            i += 1
        row_idx = i - 1
        if row_idx != -1:
            for val in matrix[row_idx]:
                if val == target:
                    return True
        return False
