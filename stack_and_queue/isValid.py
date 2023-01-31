#!/usr/bin/python3
"""Defines the Solution class"""


class Solution:
    """Solution Class"""
    @staticmethod
    def isValid(s: str) -> bool:
        """Checks if a string contains a Vaild Parenthesis"""
        stack = []
        for element in s:
            if element in ['[', '(', '{']:
                stack.append(element)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if top == '(' and element == ')':
                        continue
                    if top == '[' and element == ']':
                        continue
                    if top == '{' and element == '}':
                        continue
                    return False
                return False
        if stack:
            return False
        return True

print(Solution.isValid('()(){}]['))
