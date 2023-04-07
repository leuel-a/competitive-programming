#!/usr/bin/python3
"""LeetCode Problem #766 --> Toeplitz Matrix"""


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i + 1 < len(matrix) and j + 1 < len(matrix[i + 1]):
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False
        return True
