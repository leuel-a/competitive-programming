#!/usr/bin/python3
"""LeetCode Problem #1365 --> How Many Numbers Are Smaller Than
Current Number"""



class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        smallerArr = []

        for i in nums:
            count = 0
            for j in nums:
                if j == i:
                    continue
                if i > j:
                    count += 1
            smallerArr.append(count)
        return smallerArr
