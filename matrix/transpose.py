#!/usr/bin/python3
"""LeetCode Problem #867 --> Transpose Matrix"""


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transpose[j][i] = matrix[i][j]
        return transpose
