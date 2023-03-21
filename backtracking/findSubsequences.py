#!/usr/bin/python3
"""LeetCode Problem #491 --> Non-decreasing Subsequences"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        sequence, dict_s, curr = [], {}, []

        def backtrack(idx: int):
            if len(curr) > 1:
                if tuple(curr) not in dict_s:
                    sequence.append(curr[:])
                    dict_s[tuple(curr)] = 1

            if idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                if len(curr) == 0 or curr[-1] <= nums[i]:
                    curr.append(nums[i])
                    backtrack(i + 1)
                    curr.pop()

        backtrack(0)
        return sequence
