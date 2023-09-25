"""Leetcode Problem #1405 --> Longest Happy String"""
from typing import List
from functools import cache


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @cache
        def dp(idx: int, amount: int) -> int:
            # Add Base Case
            if idx >= len(satisfaction):
                return 0

            # Pick the current index
            pick = dp(idx + 1, amount + 1) + (satisfaction[idx] * amount)

            # Dont pick the current index
            dont_pick = dp(idx + 1, amount)

            return max(pick, dont_pick)
        val = dp(0, 1)
        return val if val != float('-inf') else 0
