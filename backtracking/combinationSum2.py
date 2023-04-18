#!/usr/bin/python3
"""LeetCode Problem #40 --> Combination Sum II"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        combs = []

        def backtrack(idx: int, curr: list[int], _sum: int) -> None:
            if idx >= len(candidates):
                return

            curr.append(
