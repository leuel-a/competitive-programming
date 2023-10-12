"""Leetcode Problem #63 --> Unique Paths II"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < m

        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = 1

        for j in range(m - 2, -1, -1):
            if obstacleGrid[-1][j] == 1:
                continue
            dp[-1][j] = dp[-1][j + 1]

        for i in range(n - 2, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue

                right = 0 if not inbound(i, j + 1) else dp[i][j + 1]
                down = 0 if not inbound(i + 1, j) else dp[i + 1][j]

                dp[i][j] = right + down

        return dp[0][0]
