"""Leetcode Problem #34 --> Find First and Last Position of Element in Sorted Array"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        # First Index Search
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if result[0] == -1:
                    result[0] = mid
                    high = mid - 1
                elif mid > result[0]:
                    high = mid - 1
                else:
                    result[0] = mid
                    high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # Last Index Search
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if result[1] == -1:
                    result[1] = mid
                    low = mid + 1
                elif mid < result[1]:
                    low = mid + 1
                else:
                    result[1] = mid
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result
