#!/usr/bin/python3
"""LeetCode #78 --> Subsets"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets, dict_s = [], {}

        subsets.append([])
        def backtrack(idx, curr: list):
            if idx > len(nums):
                return

            if len(curr) > 0 and dict_s.get(tuple(curr)) == None:
                subsets.append(curr[:])
                dict_s[tuple(curr)] = curr

            curr.append(nums[idx - 1])
            backtrack(idx + 1, curr)
            curr.pop()

            backtrack(idx + 1, curr)
        backtrack(0, [])
        return subsets
