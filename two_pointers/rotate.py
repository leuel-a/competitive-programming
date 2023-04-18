#!/usr/bin/python3
"""LeetCode Problem #189 --> Rotate Array"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def flip_array(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k = k % len(nums)
        flip_array(len(nums) - k, len(nums) - 1)
        flip_array(0, len(nums) - k - 1)
        flip_array(0, len(nums) - 1)
