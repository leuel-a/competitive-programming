#!/usr/bin/python3
"""LeetCode Problem #2426 --> Number of Pairs Satisfying Inequality"""


class Solution:
    def merge_sort(self, nums: list[int]) -> list[int]:

        def divide(left: int, right: int) -> list[int]:
            if left == right:
                return [nums[left]]

            mid = left + (right - left) // 2

            leftSide = divide(left, mid)
            rightSide = divide(mid + 1, right)
            return merge(leftSide, rightSide)

        def merge(leftSide: list[int], rightSide: list[int]) -> list[int]:
            res, leftPtr, rightPtr = [], 0, 0

            i, j = 0, 0
            while j < len(rightSide):
                while i < len(leftSide) and leftSide[i] <= rightSide[j] + self.diff:
                    i += 1
                self.count += i
                j += 1

            while leftPtr < len(leftSide) and rightPtr < len(rightSide):
                if leftSide[leftPtr] <= rightSide[rightPtr]:
                    res.append(leftSide[leftPtr])
                    leftPtr += 1
                else:
                    res.append(rightSide[rightPtr])
                    rightPtr += 1

            res.extend(leftSide[leftPtr:])
            res.extend(rightSide[rightPtr:])
            return res

        return divide(0, len(nums) - 1)


    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        nums, self.diff = [], diff
        self.count = 0

        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])

        print(self.merge_sort(nums))
        return self.count
