"""Leetcode Problem #1029 --> Two City Scheduling"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []

        for aCost, bCost in costs:
            arr.append((aCost - bCost, (aCost, bCost)))

        arr.sort()
        result = 0
        n = len(arr) // 2

        count = 1
        for diff, (aCost, bCost) in arr:
            if count > n:
                result += bCost
            else:
                result += aCost
            count += 1
        return result
