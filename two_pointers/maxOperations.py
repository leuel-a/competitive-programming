#!/usr/bin/python3
"""LeetCode Problem #1679 --> Max Number of K-Sum Pairs"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                count += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return count
