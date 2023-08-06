#!/usr/bin/python3
"""Leetcode 334 --> Increasing Triplet Subsequence"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_ = [num for num in nums]

        for i in range(len(nums) - 2, -1, -1):
            max_[i] = max(max_[i], max_[i + 1])

        left_min = nums[0]
        for j in range(1, len(nums)):
            if left_min < nums[j] < max_[j]:
                return True
            left_min = min(left_min, nums[j])
        return False
