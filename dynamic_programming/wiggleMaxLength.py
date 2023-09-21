"""Leetcode Problem #376 --> Wiggle Subsequence"""
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] == nums[j]:
                    continue
                
                if nums[i] < nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                else:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        a, b = dp[-1]
        return max(a, b)
