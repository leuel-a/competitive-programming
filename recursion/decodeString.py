#!/usr/bin/python3
"""LeetCode Problem #394 --> Decode String"""


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        def generate_string(idx: int) -> str:
            nonlocal res

            if idx >= len(s):
                return ""

            if s[idx] == ']':
                return ""

            for i in range(idx, len(s)):
                if s[i].isnumeric():
                    res += int(s[idx]) * generate_string(i + 2)
                res += s[i] + generate_string(i + 1)

        generate_string(0)
        return ''


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
