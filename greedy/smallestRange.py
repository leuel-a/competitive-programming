"""Leetcode Problem #908 --> Smallest Range I"""
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2 * k, 0)
