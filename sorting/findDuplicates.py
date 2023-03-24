#!/usr/bin/python3
"""LeetCode Problem #442 --> Find All Duplicates in an Array"""

class Solution:
    def findDuplicates(self, nums: list) -> list:
        duplicates, i = [], 0

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
                duplicates.append(num)
        return duplicates
