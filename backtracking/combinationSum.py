#!/usr/bin/python3
"""LeetCode #49 --> Combination Sum"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs, dict_s = [], {}

        def backtrack(idx: int, curr: List[int], _sum: int) -> None:
            if _sum == target:
                if tuple(curr) not in dict_s:
                    combs.append(curr[:])
                    dict_s[tuple(curr)] = 1

            if idx >= len(candidates):
                return

            curr.append(candidates[idx])
            _sum += candidates[idx]
            if _sum <= target:
                backtrack(idx, curr, _sum)
            _sum -= candidates[idx]
            curr.pop()

            backtrack(idx + 1, curr, _sum)

        backtrack(0, [], 0)
        return combs
