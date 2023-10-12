"""Leetcode Problem #57 --> Insert Interval"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        stack = []
        for start, end in intervals:
            if stack:
                a, b = stack.pop()
                if a <= start <= b:
                    stack.append([min(start, a), max(b, end)])
                else:
                    stack.append([a, b])
                    stack.append([start, end])
            else:
                stack.append([start, end])
        return stack
