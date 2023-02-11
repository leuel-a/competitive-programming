#!/usr/bin/python3
"""Defines the Solution Class"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Solution Class for LeetCode Problem #11"""
        maxVolume, i, j = 0,  0,  len(height) - 1
        while j >= i:
            maxVolume = max(maxVolume, (j - i) * min(height[i], height[j]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxVolume
