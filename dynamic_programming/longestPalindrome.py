"""Leetcode Problem #5 --> Longest Palindromic Substring"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_ = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_ = [i, i + 1]

        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_ = [i, j]
        left, right = max_
        return s[left:right+1]
