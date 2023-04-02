#!/usr/bin/python3
"""LeetCode Problem #46 --> Permutations"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        used = 0

        permutations = []
        def backtrack(curr: list[int]) -> None:
            nonlocal used
            if len(curr) == len(nums):
                permutations.append(curr[:])
                return

            for j, num in enumerate(nums):
                if (used & (1 << j)) == 0:
                    used |= 1 << j
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    used ^= 1 << j
        backtrack([])
        return permutations
