#!/usr/bin/python3
"""LeetCode Problem #125 --> Valid Palindrome"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPalindromeHelper(s: str, left: int, right: int):
            if left >= right:
                return True

            if s[left].casefold() != s[right].casefold():
                return False            
            return isPalindromeHelper(s, left + 1, right - 1)
        new_str = re.sub(r'[\W_]', '', s)        
        return isPalindromeHelper(new_str, 0, len(new_str) - 1)
