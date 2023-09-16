"""Leetcode Problem #566 --> Reshape the Matrix"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])

        if (rows * columns) != (r * c):
            return mat

        result = [[0 for _ in range(c)] for _ in range(r)]
        result_row = result_col = 0
        for i in range(rows):
            for j in range(columns):
                result[result_row][result_col] = mat[i][j]
                result_col += 1
                
                if result_col == c:
                    result_col = 0
                    result_row += 1
        return result