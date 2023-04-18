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


a = [1, 0, 1]
b = [0, 0, 0]
c = [0, 0, 0, 0]
for i in range(len(a) -1, -1, -1):
    _sum = a[i] + b[i] + c[i + 1]
    if _sum >= 2:
        c[i] = 1
        c[i + 1] = _sum - 2
    else:
        c[i + 1] = _sum
print(c)
