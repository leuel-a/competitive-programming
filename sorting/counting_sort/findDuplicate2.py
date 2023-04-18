#!/usr/bin/python3
"""LeetCode Problem #287 --> Find the Duplicate Number"""


class Solution:
    def findDuplicate(self, nums: list) -> list:
        i = 0

        while i < len(nums):
            pos = nums[i] - 1
            if pos != i:
                if nums[pos] != nums[i]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                else:
                    i += 1
            else:
                i += 1

        for index, num in enumerate(nums):
            if num != index + 1:
                return num
