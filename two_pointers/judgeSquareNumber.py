#!/usr/bin/python3
"""LeetCode Problem #633 --> Sum of Squared Numbers"""
from math import floor, sqrt
from typing import List, Optional


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, floor(sqrt(c))

        while low <= high:
            val = low ** 2 + high ** 2
            if val == c:
                return True

            if val > c:
                high -= 1
            else:
                low += 1
        return False

