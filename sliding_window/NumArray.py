#!/usr/bin/python3
"""LeetCode Problem #303 --> Range Sum Query - Immutable

Description:
    Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between
    indices left and right inclusive where left <= right.

    Implement the NumArray class:

        => NumArray(int[] nums) Initializes the object with the
            integer array nums.

        => int sumRange(int left, int right)
            Returns the sum of the elements of nums between
            indices left and right inclusive
            (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums[:]

    def sumRange(self, left: int, right: int) -> int:
        prefixSum, curr_sum = [], 0
        
        prefixSum.append(curr_sum)
        for num in self.nums:
            curr_sum += num
            prefixSum.append(curr_sum)

        return prefixSum[right + 1] - prefixSum[left]
