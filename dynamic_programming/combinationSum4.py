#!/usr/bin/python3
"""LeetCode Problem #377 --> Combination Sum IV"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # Using TOP-DOWN Approach
        # @cache
        # def dp(curr: int) -> int:
        #     if curr == 0:
        #         return 1

        #     result = 0
        #     for num in nums:
        #         if curr - num >= 0:
        #             result += dp(curr - num)
        #     return result

        # return dp(target)

        # Using BOTTOM-UP Approach
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
