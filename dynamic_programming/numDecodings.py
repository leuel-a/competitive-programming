#!/usr/bin/python3
"""LeetCode Problem #91 --> Decode Ways"""


class Solution:
    def numDecodings(self, s: str) -> int:
        _cache = { len(s): 1 }

        def dp(idx: int) -> int:
            if idx in _cache:
                return _cache[idx]

            if s[idx] == '0':
                return 0

            curr = dp(idx + 1)
            if idx + 1 < len(s) and int(s[idx: idx+2]) < 27:
                curr += dp(idx + 2)
            _cache[idx] = curr
            return _cache[idx]
        return dp(0)
