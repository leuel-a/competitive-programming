#!/usr/bin/python3
"""LeetCode Problem #209 --> Minimum Size Subarray Sum

Description:
    Given an array of positive integers nums and a positive
    integer target, return the minimal length of a subarray
    whose sum is greater than or equal to target. If there
    is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = end = curr_sum = 0
        minSize = float('inf')
        while end < len(nums):
            curr_sum = nums[end]
            end = end + 1

            while start <= end and curr_sum >= target:
                curr_sum = curr_sum - nums[start]
                start = start + 1

                minSize = min(minSize, end - start + 1)

        if minSize == float('inf'):
            minSize = 0

        return minSize
