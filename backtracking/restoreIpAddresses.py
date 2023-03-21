#!/usr/bin/python3
"""LeetCode Problem #93 --> Restore IP Addresses"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ips = []

        def backtrack(idx: int, curr: list) -> None:
            if len(curr) > 4:
                return

            if idx >= len(s):
                if len(curr) == 4:
                    valid_ips.append('.'.join(curr))
                return

            for i in range(idx, len(s)):
                val = s[idx:i+1]

                if val != str(int(val)):
                    return

                if 0 <= int(val) <= 255:
                    curr.append(val)
                    print(curr)
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return valid_ips
