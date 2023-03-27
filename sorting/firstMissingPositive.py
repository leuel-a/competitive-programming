#!/usr/bin/python3
"""LeetCode Problem #First Missing Positive"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            correct_pos = nums[i] - 1

            if correct_pos != i and 0 <= correct_pos < len(nums) and nums[correct_pos] != nums[i]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        for j in range(len(nums)):
            if nums[j] - 1 != j:
                return j + 1
        return len(nums) + 1

