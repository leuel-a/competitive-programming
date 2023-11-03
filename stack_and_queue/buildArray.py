"""Leetcode Problem #1441 --> Build an Array With Stack Operations"""
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        result = []

        i = 0
        stream = 1
        while stream < n + 1 and i < len(target):
            stack.append(stream)
            result.append("Push")
            if stack[-1] != target[i]:
                stack.pop()
                result.append("Pop")
            else:
                i += 1
            stream += 1
        return result
