#!/usr/bin/python3
"""LeetCode Problem #2140 --> Solving Questions With Brainpower"""
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions))]

        def inbound(idx: int):
            return idx < len(questions)

        for i in range(len(dp) - 1, -1, -1):
            points, brainpower = questions[i]
            solve = points + (dp[i + brainpower + 1] if inbound(i + brainpower + 1) else 0)
            dont_solve = dp[i + 1] if inbound(i + 1) else 0
            dp[i] = max(solve, dont_solve)
        return dp[0]
