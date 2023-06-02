#!/usr/bin/python3
"""LeetCode Problem #1509 --> Minimum Difference Between Largest and Smallest Value in Three Moves"""
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 4:
            return 0
        # Case 1: change three smallest elements to largest element
        diff1 = nums[n-1] - nums[3]
        # Case 2: change two smallest elements to second largest element, and one largest element to smallest element
        diff2 = nums[n-2] - nums[2]
        # Case 3: change one smallest element to third largest element, and two largest elements to second smallest element
        diff3 = nums[n-3] - nums[1]
        # Case 4: change three largest elements to smallest element
        diff4 = nums[n-4] - nums[0]
        return min(diff1, diff2, diff3, diff4)
