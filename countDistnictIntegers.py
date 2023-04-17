#!/usr/bin/python3
"""LeetCode Problem #2442 --> Count Number of Distnict Integers After Reversing Operation"""
from collections import Counter


class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        reverse_nums = []

        for num in nums:
            reverse_nums.append(int(str(num)[::-1]))
        nums.extend(reverse_nums)
        return len(Counter(nums))
