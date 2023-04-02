#!/usr/bin/python3
"""LeetCode Problem #2406 --> Apply Operations to an Array"""


class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        count = 0
        for num in nums:
            if num != 0:
                nums[count] = num
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1
        return nums
