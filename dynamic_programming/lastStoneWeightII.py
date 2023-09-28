"""Leetcode Problem #1049 --> Last Stone Weight II"""
from typing import List
from math import ceil


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones)
        target = ceil(stonesSum / 2)

        def dfs(i: int, total: int):
            if total >= target or i == len(stones):
                return abs(total - (stonesSum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))
            return dp[(i, total)]
        dp = {}
        return dfs(0, 0)