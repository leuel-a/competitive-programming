"""LeetCode Problem #33 --> Search in Rotated Sorted Array"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left, right = 0, n - 1
        while right > left + 1:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if target <= nums[right] and target >= nums[mid]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1
