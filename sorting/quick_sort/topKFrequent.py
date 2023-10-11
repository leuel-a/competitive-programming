"""Leetcode Problem #347 --> Top K Frequent Elements"""
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = None
        numCount = Counter(nums)

        nums = [(num, count) for num, count in numCount.items()]

        def quick_select(start: int, end: int) -> List[int]:
            pivotFreq, write = nums[start][1], start + 1

            for read in range(start + 1, len(nums)):
                value, freq = nums[read]

                if freq < pivotFreq:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1

            nums[start], nums[write - 1] = nums[write - 1], nums[start]

            if k == len(nums) - (write - 1):
                result = []
                for i in range(write - 1, len(nums)):
                    num, freq = nums[i]
                    result.append(num)
                return result
            if k < len(nums) - (write - 1):
                return quick_select(write, end)
            return quick_select(start, write - 2)
        return quick_select(0, len(nums) - 1)
