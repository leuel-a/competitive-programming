#!/usr/bin/python3
"""LeetCode Problem #315 --> Count of Smaller Numbers After Self"""


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        self.count_array = [0] * len(nums)

        self.merge_sort(nums)
        return self.count_array

    def merge_sort(self, nums: list[int]) -> list[int]:

        def divide(left: int, right: int) -> list[int]:
            if right == left:
                return [(nums[left], left)]

            mid = left + (right - left) // 2

            left_side = divide(left, mid)
            right_side = divide(mid + 1, right)
            return merge(left_side, right_side)

        def merge(left_side: list[int], right_side: list[int]) -> list[int]:
            res = []
            left, right = 0, 0

            i, j = 0, 0
            while i < len(left_side):
                while j < len(right_side) and left_side[i][0] > right_side[j][0]:
                    j += 1
                self.count_array[left_side[i][1]] += j
                i += 1

            while left < len(left_side) and right < len(right_side):
                if left_side[left] <= right_side[right]:
                    res.append(left_side[left])
                    left += 1
                else:
                    res.append(right_side[right])
                    right += 1

            res.extend(left_side[left:])
            res.extend(right_side[right:])
            return res

        return divide(0, len(nums) - 1)
