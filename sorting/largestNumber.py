#!/usr/bin/python3
"""LeetCode Problem #179 Largest Number"""
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                case1 = int(str(nums[i]) + str(nums[j]))
                case2 = int(str(nums[j]) + str(nums[i]))

                if case1 < case2:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int(''.join(map(str, nums))))
