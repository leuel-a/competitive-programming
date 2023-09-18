"""Leetcode Problem #516 --> Longest Palindromic Subsequence"""
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]

        n = len(s)
        c = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])
        return c[n][n]