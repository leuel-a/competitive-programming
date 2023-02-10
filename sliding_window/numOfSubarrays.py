#!/usr/bin/python3
"""Defines the Solution Class"""

class Solution:
    """Solution Class for LeetCode Problem #1343"""
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        greater_than_threshold, i, j, curr_sum = 0, 0, 0, 0
        while j < len(arr):
            curr_sum += arr[j]
            while j - i + 1 > k:
                curr_sum -= arr[i]
                i += 1
            if j - i + 1 == k:
                average = curr_sum / k
                if average >= threshold:
                    greater_than_threshold += 1
            j += 1
        return greater_than_threshold
