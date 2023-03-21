#!/usr/bin/python3
"""LeetCode Problem #75 --> Sort Colors"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, elem in enumerate(nums):
            jMin = i

            for j in range(i + 1, len(nums)):
                if nums[jMin] > nums[j]:
                    jMin = j

            if jMin != i:
                nums[jMin], nums[i] = nums[i], nums[jMin]
