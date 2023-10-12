"""Leetcode Problem #2871 --> Split Array Into Maximum Number of Subarrays"""
from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for n in nums:
            cur = n if cur == 0 else cur & n
            res += (cur == 0)
        return max(1, res)
