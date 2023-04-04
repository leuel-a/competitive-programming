#!/usr/bin/python3
"""LeetCode Problem #2447 --> Number of Subarrays With GCD Equal to K"""


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        def gcd(a, b=0):
            if b == 0:
                return a
            return gcd(b, a % b)

        i = j = count = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                currGCD = gcd(nums[i])
                if currGCD == k:
                        count += 1
                j = i + 1
                while j < len(nums) and nums[j] % k == 0:
                    currGCD = gcd(currGCD, nums[j])
                    if currGCD == k:
                        count += 1
                    j += 1
        return count
