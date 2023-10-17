"""Leetcode Problem #935 --> Knight Dialer"""
from typing import List


class Solution:
    def knightDialer(self, n: int) -> int:
        k, m = 4, 3

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < k and 0 <= col < m

        # These are the directions that the knight can go
        directions = [
            (1, 2), (1, -2),
            (-1, 2), (-1, -2),
            (2, 1), (2, -1),
            (-2, 1), (-2, -1)
        ]

        prev = [[0] * m for _ in range(k)]
        curr = [[0] * m for _ in range(k)]

        invalid = set([(3, 0), (3, 2)])

        # Resets a matrix to the values that are equal to zero
        def reset(matrix: List[List[int]]) -> None:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        def deepCopy(first: List[List[int]], second: List[List[int]]) -> None:
            for i in range(len(first)):
                for j in range(len(first[0])):
                    first[i][j] = second[i][j]

        # Set the initial values in the matrix
        for i in range(k):
            for j in range(m):
                if (i, j) not in invalid:
                    prev[i][j] = 1

        for _ in range(1, n):
            for i in range(k):
                for j in range(m):
                    currVal = prev[i][j]
                    currRow, currCol = i, j

                    for rInc, cInc in directions:
                        newRow, newCol = currRow + rInc, currCol + cInc

                        if inbound(newRow, newCol) and (newRow, newCol) not in invalid:
                            curr[newRow][newCol] += currVal

            deepCopy(prev, curr)
            reset(curr)

        result = 0
        MOD = pow(10, 9) + 7

        for i in range(k):
            for j in range(m):
                result += prev[i][j]
        return result % MOD
