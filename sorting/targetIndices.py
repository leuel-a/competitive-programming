#!/usr/bin/python
"""Soultion class contains solution for --> Find Target Indices After Sorting Array

Description:
    You are given a 0-indexed integer array nums and a target element target.
        A target index is an index i such that nums[i] == target.

    Return a list of the target indices of nums after sorting nums in non-decreasing order.
        If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetList = []
        index = 0
        for i in sorted(nums):
            if i == target:
                targetList.append(index)
            index += 1
        return targetList
