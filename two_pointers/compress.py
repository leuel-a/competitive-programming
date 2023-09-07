#!/usr/bin/python3
"""Leetcode Problem #443 --> String Compression"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0

        while i < len(chars):
            group_length = 1

            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1

            if group_length > 1:
                str_rep = str(group_length)
                chars[res:res+len(str_rep)] = list(str_rep)
                res += len(str_rep)

            i += group_length
        return res