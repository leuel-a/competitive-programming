#!/usr/bin/python3
"""LeetCode #2305 --> Fair Distribution of Cookies"""

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        bucket = [0]*k
        minUnfairness = float('inf')

        def backtrack(i,bucket):
            nonlocal minUnfairness
            if i >= len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return

            for j in range(k):
                bucket[j] += cookies[i]
                if bucket[j] < minUnfairness:
                    backtrack(i+1, bucket)
                bucket[j] -= cookies[i]

        backtrack(0, bucket)
        return minUnfairness
