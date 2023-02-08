#!/usr/bin/python3
"""Defines the Solution Class"""

class Solution:
    """Solution Class for LeetCode problem #1190"""
    def reverseParentheses(self, s: str) -> str:
        """Reverses a string based on parentheses"""
        stack = []
        result = ''
        for char in s:
            if char in [')']:
                temp = ""
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                for i in temp:
                    stack.append(i)
                continue
            stack.append(char)

        for i in stack:
            result += i
        return result
