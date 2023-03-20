#!/usr/bin/python3
"""LeetCode Problem #1283 --> Find the Smallest Divisor in a Given Threshold"""


class Solution:
    def sumDivisor(self, nums: List[int], divisor: int) -> int:
        _sum = 0
        for num in nums:
            _sum += ceil(num / divisor)
        return _sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        while low <= high:
            mid = low + (high - low) // 2

            if self.sumDivisor(nums, mid) > threshold:
                low = mid + 1
            elif self.sumDivisor(nums, mid) <= threshold:
                high = mid - 1
        return low
