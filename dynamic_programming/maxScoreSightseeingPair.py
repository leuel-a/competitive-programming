#!/usr/bin/python3
"""LeetCode Problem #1014 --> Best Sightseeing Pair"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        iMax = [values[0]]
        for i in range(1, len(values)):
            iMax.append(max(iMax[-1], i + values[i]))

        max_ = -1
        for j in range(1, len(values)):
            max_ = max(iMax[j - 1] + values[j] - j, max_)
        return max_ if len(values) > 2 else values[0] + values[1] - 1
