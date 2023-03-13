#!/usr/bin/python3
"""LeetCode #852 --> Peak Index in a Mountain Array"""


class Solution:
    def peakIndexInMountainArray(self, arr: list(int)) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid + 1] > arr[mid]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                return mid
        return low
