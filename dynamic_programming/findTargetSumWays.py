#!/usr/bin/python3
"""LeetCode Problem #494 --> Target Sum"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def findPossibleWays(idx: int, running_sum: int, operation=None) -> int:
            if idx == len(nums):
                return running_sum == target

            if (idx, running_sum, operation) in memo:
                return memo[(idx, running_sum, operation)]

            result = 0
            # Decide to add the current index
            result += findPossibleWays(idx + 1, running_sum + nums[idx], '+')

            # Decide not to deduct from the current sum
            result += findPossibleWays(idx + 1, running_sum - nums[idx], '-')

            memo[(idx, running_sum, operation)] = result
            return result
        return findPossibleWays(0, 0)
