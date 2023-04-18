#!/usr/bin/python3
"""LeetCode Problem #215 --> Kth Largest Element in an Array"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def findKthLargestHelper(start, end) -> int:
            pivot, write = nums[start], start + 1
            for read in range(start + 1, len(nums)):
                if nums[read] < pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1

            nums[start], nums[write - 1] = nums[write - 1], nums[start]

            if k == (len(nums) - (write - 1)):
                return nums[write - 1]
            elif k < (len(nums) - (write - 1)):
                return findKthLargestHelper(write, end)
            return findKthLargestHelper(start, write - 2)
        return findKthLargestHelper(0, len(nums) - 1)
