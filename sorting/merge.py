"""Leetcode Problem #56 --> Merge Intervals"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for start, end in intervals:
            if stack:
                a, b = stack.pop()

                if a <= start <= b:
                    stack.append([min(a, start), max(end, b)])
                else:
                    stack.append([a, b])
                    stack.append([start, end])
            else:
                stack.append([start, end])

        return stack
