"""Leetcode Problem #977 --> Squares of a Sorted Array"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_squares = [0 for _ in range(n)]

        # This is a really interesting two pointer problem

        k = n - 1
        i, j = 0, n - 1
        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                sorted_squares[k] = nums[i] ** 2
                i += 1
            else:
                sorted_squares[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return sorted_squares
