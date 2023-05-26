#!/usr/bin/python3
"""LeetCode Problem #1646 --> Get Maximum in Generated Array"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        memo = {0: 0, 1: 1}

        def dp(i: int) -> int:
            # Base Case
            if i in memo:
                return memo[i]

            # Check if we have our solution for the current sub-problem
            # in our memory
            if i % 2 == 0:
                memo[i] = dp(i // 2)
            else:
                memo[i] = dp(i // 2) + dp(i // 2 + 1)
            return memo[i]

        for i in range(n + 1):
            nums.append(dp(i))
        return max(nums)
            
