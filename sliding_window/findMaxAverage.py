#!/usr/bin/python3
"""LeetCode Problem #643 --> Maximum Average Subarray I

Description:
    You are given an integer array nums consisting of n elements,
    and an integer k.

    Find a contiguous subarray whose length is equal to k that has
    the maximum average value and return this value. Any answer
    with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i, j = 0, 0
        sum, average = 0, 0
        maxAverage = float('-inf')
        while j < len(nums):
            sum += nums[j]
            while j - i + 1 > k:
                sum -= nums[i]
                i += 1
            if j - i + 1 == k:
                average = sum / k
                maxAverage = max(maxAverage, average)
            j += 1
        return maxAverage

sol = Solution()
print(sol.findMaxAverage([-1], 1))
