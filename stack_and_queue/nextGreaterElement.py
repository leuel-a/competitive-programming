#!/usr/bin/python3
"""Defines the Solution class"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = []
        for number in nums1:
            target = number
            for i, elem in enumerate(nums2):
                if target == elem:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > elem:
                            next_greater.append(nums2[j])
                            break
                    else:
                        next_greater.append(-1)
        return next_greater

