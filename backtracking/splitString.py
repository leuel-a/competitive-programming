#!/usr/bin/python3
"""LeetCode #1849 --> Splitting a String Into Descending Consecutive Values"""

class Solution:
    def splitString(self, s: str):
        current = []

        def backtrack(idx):
            if idx >= len(s):
                return idx >= len(s)

            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if len(current) == 0 or current[-1] - val == -1:
                    current.append(val)
                    if backtrack(idx + 1):
                        return True
                    current.pop()
            return False
        return backtrack(0)


