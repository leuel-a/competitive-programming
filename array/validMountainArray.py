#!/usr/bin/python3
"""LeetCode Problem #941 --> Valid Mountain Array"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or arr[0] >= arr[1]:
            return False

        peakFound, i = False, 2
        while i < len(arr):
            if peakFound:
                if arr[i] >= arr[i - 1]:
                    return False
            else:
                if arr[i] < arr[i - 1]:
                    peakFound = True
                elif arr[i] == arr[i - 1]:
                    return False
            i += 1
        return peakFound
