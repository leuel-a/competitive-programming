"""Leetcode Problem #416 --> Partition Equal Subset Sum"""
from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)

        if sum_ % 2 != 0:
            return False

        target = sum_ / 2

        @cache
        def dp(idx: int, curr: int) -> bool:
            nonlocal target
            if idx >= len(nums):
                return False

            if curr == target:
                return True

            if curr > target:
                return False

            if dp(idx + 1, curr + nums[idx]):
                return True

            if dp(idx + 1, curr):
                return True
            return False
        return dp(0, 0)
