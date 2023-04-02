#!/usr/bin/python3
"""LeetCode Problem #1299 --> Replace Elements with Greatest Element on Right Side"""


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = [-1] * len(arr)
        greatest_right = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i + 1] > greatest_right:
                greatest_right = arr[i + 1]
            result[i] = greatest_right
        return result
