#!/usr/bin/python3
"""LeetCode Problem #1962 --> Remove Stones to Minimize the Total"""
from heapq import heapify, heappop, heappush
from math import floor
from typing import list


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-val for val in piles]

        heapify(piles)
        for i in range(k):
            val = heappop(piles)
            val = -1 * (-val - floor(-val / 2))
            heappush(piles, val)
        return -1 * sum(piles)
