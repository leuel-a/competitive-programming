"""Leetcode Problem #54 --> Spiral Matrix"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        visited = set()
        n, m = len(matrix), len(matrix[0])

        row, col = 0, 0
        curr_dir = 'R'
        while len(result) != n * m:
            if curr_dir == 'R':
                if col == m or (row, col) in visited:
                    col -= 1
                    row += 1
                    curr_dir = 'D'
                    continue
                result.append(matrix[row][col])
                visited.add((row, col))
                col += 1
            elif curr_dir == 'D':
                if row == n or (row, col) in visited:
                    row -= 1
                    col -= 1
                    curr_dir = 'L'
                    continue
                result.append(matrix[row][col])
                visited.add((row, col))
                row += 1
            elif curr_dir == 'L':
                if col == -1 or (row, col) in visited:
                    col += 1
                    row -= 1
                    curr_dir = 'U'
                    continue
                result.append(matrix[row][col])
                visited.add((row, col))
                col -= 1
            elif curr_dir == 'U':
                if row == -1 or (row, col) in visited:
                    row += 1
                    col += 1
                    curr_dir = 'R'
                    continue
                result.append(matrix[row][col])
                visited.add((row, col))
                row -= 1
        return result