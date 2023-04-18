#!/usr/bin/python3
"""LeetCode Problem #88 --> Merge Sorted Array"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        print(nums1)
        def quick_sort(start: int, end: int):
            if end - start < 0:
                return

            pivot, write = nums1[start], start + 1
            for read in range(start + 1, end + 1):
                if nums1[read] <= pivot:
                    nums1[read], nums1[write] = nums1[write], nums1[read]
                    write += 1

            nums1[start], nums1[write - 1] = nums1[write - 1], nums1[start]
            quick_sort(start, write - 2)
            quick_sort(write, end)

        quick_sort(0, len(nums1) - 1)
