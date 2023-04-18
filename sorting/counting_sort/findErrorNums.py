#!/usr/bin/python3
"""LeetCode Problem #645 --> Set Mismatch"""


class Solution:
    def findErrorNums(self, nums: list) -> list:
        set_mis_match, i = [], 0

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
                set_mis_match = [num, index + 1]
                break
        return set_mis_match
