#!/usr/bin/python3
"""LeetCode Problem #213 --> House Robber"""
from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index: int, first_state: bool = False) -> int:
            if first_state and index == len(nums) - 1:
                return 0 if first_state else nums[index]

            if index >= len(nums):
                return 0

            choose = nums[index] + dp(index + 2, True if first_state or index == 0 else False)
            not_choose = dp(index + 1, first_state)
            return max(choose, not_choose)
        return dp(0)
