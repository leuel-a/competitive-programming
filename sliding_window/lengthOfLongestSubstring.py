#!/usr/bin/python3
"""Defines the Solution Class"""


class Solution:
    """Solution Class for LeetCode Problem #3"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest sub string in a string
        with no repeating characters in the sub string"""
        sub_string, j, max_length = [], 0, 0
        for ind, elem in enumerate(s):
            while j <= ind and elem in sub_string:
                j += 1
                sub_string.pop(0)
            sub_string.append(elem)
            max_length = max(max_length, len(sub_string))
        return max_length
