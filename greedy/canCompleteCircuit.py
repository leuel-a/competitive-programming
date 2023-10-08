"""Leetcode Problem #134 --> Gas Station"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]

        if sum(diff) < 0:
            return -1
        
        curr = 0
        start = 0
        for i, g in enumerate(diff):
            curr += g
            if curr < 0:
                curr = 0
                start = i + 1
        return start