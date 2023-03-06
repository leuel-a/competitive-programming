#!/usr/bin/python3
"""LeetCode Problem #1480 -> Running Sum of 1d Array"""

class Solution:
    def runningSum(self, nums: list[int]) -> int:
        prefixSum = []

        prefixSum.append(nums[0])
        curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum += num
            prefixSum.append(curr_sum)

        return prefixSum
