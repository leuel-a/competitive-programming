#!/usr/bin/python3
"""LeetCode Problem #746 --> Min Cost Climbing Stairs"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(idx: int) -> int:
            # Base Case
            if idx >= len(cost):
                return 0

            # If I already know my value in my memo, then I just return it.
            if idx in memo:
                return memo[idx]

            # If I choose to take climb one step, or two tep, I need
            # to calculate the output for both and calculate my solution
            # from there.

            one_step = dp(idx + 1)
            two_step = dp(idx + 2)
            memo[idx] = min(one_step, two_step) + cost[idx]

            return memo[idx]
        dp(0)
        return min(memo[0], memo[1])

