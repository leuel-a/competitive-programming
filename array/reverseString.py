#!/usr/bin/python3
"""LeetCode Problem #344 --> Reverse String"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revStrHelper(s: list[str], left: int, right: int) -> None:
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            return revStrHelper(s, left + 1, right - 1)
        revStrHelper(s, 0, len(s) - 1)
        return s
