#!/usr/bin/python3
"""LeetCode #278 First Bad Version"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        if isBadVersion(left) and isBadVersion(right):
            return left

        while right - left > 1:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return right
