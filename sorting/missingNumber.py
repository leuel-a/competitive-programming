#!/usr/bin/python3
"""LeetCode Problem #268 --> Missing Number"""


class Solution:
    def missingNumber(self, nums: list) -> int:
        i = 0
        for i in range(len(nums)):
            pos = nums[i]
            if  pos != i:
                if 0 <= pos < len(nums):
                    nums[pos], nums[i] = nums[i], nums[pos]
                else:
                    continue

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
