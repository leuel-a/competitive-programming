#!/usr/bin/python3
"""LeetCode Problem #268 --> Missing Number"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = 0
        miss = 0
        for i in range(len(nums) + 1):
            total ^= i
        for num in nums:
            miss ^= num
        return total ^ miss
