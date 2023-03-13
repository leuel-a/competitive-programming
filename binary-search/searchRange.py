#!/usr/bin/python3
"""LeetCode Problem #34 --> Find First and Last Position of Element in Sorted Array

"""


class Solution:

    def binarySearch(self, nums: list[int], target: int, low: int, high: int):

        if low > high:
            return -1

        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return [low, mid]
        return self.binarySearch(nums, target, low, high)



    def searchRange(self, nums: list[int], target: int) -> list[int]:
        pass

sol = Solution()
print(sol.binarySearch([5,7,7,8,8,10], 8, 0, 5))

