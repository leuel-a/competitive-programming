"""Leetcode Problem #1626 --> Best Team With No Conflicts"""
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[j][0] for j in range(len(scores))]

        for i in range(len(scores)):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dp[i] = max(dp[i], dp[j] + mScore)
        return max(dp)
