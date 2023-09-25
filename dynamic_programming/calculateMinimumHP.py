"""Leetcode Problem #174 --> Dungeon Game"""
from typing import List
from functools import cache


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        def inbound(r: int, c: int) -> bool:
            return 0 <= r < len(dungeon) and 0 <= c < len(dungeon[0])

        @cache
        def dp(row: int, col: int) -> int:
            if row == len(dungeon) - 1 and col == len(dungeon[0]) - 1:
                return -dungeon[row][col]

            curr = float('inf')
            if inbound(row + 1, col):
                curr = min(curr, dp(row + 1, col))

            if inbound(row, col + 1):
                curr = min(curr, dp(row, col + 1))

            if dungeon[row][col] < 0 and curr < 0:
                return -dungeon[row][col]

            return curr - dungeon[row][col]
        return max(1, dp(0, 0) + 1)
