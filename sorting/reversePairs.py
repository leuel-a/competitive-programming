#!/usr/bin/python3
"""LeetCode Problem #493 --> Reverse Pairs"""


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        self.count = 0

        def divide(left: int, right: int) -> list[int]:
            if left - right == 0:
                return [nums[left]]
            mid = left + (right - left) // 2

            leftSide = divide(left, mid)
            rightSide = divide(mid + 1, right)
            return merge(leftSide, rightSide)


        def merge(leftSide: list[int], rightSide: list[int]) -> list[int]:
            res = []
            leftPtr, rightPtr = 0, 0

            i, j = 0, 0
            while j < len(rightSide):
                while i < len(leftSide) and leftSide[i] <= 2 * rightSide[j]:
                    i += 1
                if i < len(leftSide):
                    self.count += len(leftSide) - i
                else:
                    break
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

        print(divide(0, len(nums) - 1))
        return self.count
