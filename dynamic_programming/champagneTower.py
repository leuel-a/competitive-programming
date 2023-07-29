#!/usr/bin/python3
"""LeetCode Problem #799 --> Champagne Tower"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        for i in range(100):
            if i == query_row:
                break
            curr = [0 for _ in range(len(prev) + 1)]
            for j in range(len(curr)):
                if j - 1 >= 0 and prev[j - 1] > 1:
                    curr[j] += (prev[j - 1] - 1) / 2
                if j < len(prev) and prev[j] > 1:
                    curr[j] += (prev[j] - 1) / 2
            prev = curr
        return 1 if prev[query_glass] >= 1 else prev[query_glass]
