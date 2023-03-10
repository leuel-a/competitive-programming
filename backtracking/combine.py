#!/usr/bin/python3
"""LeetCode Problem #77 --> Combinations"""

class Solution:
    def combine(self, n: int, k:int):
        combinations, curr = [], []

        def backtrack(start: int):
            if len(curr) == k:
                combinations.append(curr[:])
                return

            for canidate in range(start, n + 1):
                curr.append(canidate)
                backtrack(canidate + 1)
                curr.pop()
        backtrack(1)
        return combinations

sol = Solution()
print(sol.combine(4, 2))
