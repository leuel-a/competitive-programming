#!/usr/bin/python3
"""LeetCode Problem #1239 --> Maximum Length of a Concatenated String with Unique Characters"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        curr, max_len = [], 0

        def backtrack(idx: int, bitmask: int) -> None:
            nonlocal max_len
            if len(curr) > 0:
                _str = ''.join(val for val in curr)
                max_len = max(max_len, len(_str))
            
            if idx >= len(arr):
                return
            
            check, valid = 0, True
            for char in arr[idx]:
                if check & 1 << ord(char) - 97 != 0:
                    valid = False
                    break
                check |= 1 << ord(char) - 97

            if valid and bitmask & check == 0:
                bitmask |= check
                curr.append(arr[idx])
                backtrack(idx + 1, bitmask)
                curr.pop()
                bitmask ^= check
            backtrack(idx + 1, bitmask)        
        backtrack(0, 0)
        return max_len
