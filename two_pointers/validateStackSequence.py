#!/usr/bin/python3
"""Defines the Solution Class"""

class Solution:
    """Defines the solution class for LeetCode Problem #946"""
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """Validates a stack sequence"""
        stack, k = [], 0
        for push in pushed:
            stack.append(push)
            while stack and k < len(popped) and stack[-1] == popped[k]:
                stack.pop()
                k +=  1
        return k == len(popped)
