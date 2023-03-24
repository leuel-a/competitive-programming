#!/usr/bin/python3
"""LeetCode Problem #448 --> Find All Numbers Disappeared in an Array"""

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        disappeared_nums, i = [], 0

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
                disappeared_nums.append(index + 1)
        return disappeared_nums
