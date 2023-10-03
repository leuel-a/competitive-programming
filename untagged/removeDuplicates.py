"""Leetcode Problem #1209 --> Remove All Adjacent Duplicates in String II"""
from typing import List


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                char_prev, count_prev = stack.pop()
                count_new = count_prev + 1
                if count_new < k:
                    stack.append((char, count_new))
            else:
                stack.append((char, 1))

        return ''.join([char * count for char, count in stack])
