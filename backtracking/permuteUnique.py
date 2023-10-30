"""Leetcode Problem #47 - Permutations II"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()

        def backtrack(idx: int, curr: List[int], bitmask: int) -> None:
            if len(curr) == len(nums):
                curr_str = ''.join(str(val) for val in curr)
                if curr_str not in seen:
                    seen.add(curr_str)
                    result.append(curr[:])
                return

            if idx >= len(nums):
                return

            for j in range(len(nums)):
                if bitmask & (1 << j) == 0:
                    bitmask |= 1 << j
                    curr.append(nums[j])
                    backtrack(j, curr, bitmask)
                    curr.pop()
                    bitmask ^= 1 << j
        backtrack(0, [], 0)
        return result
