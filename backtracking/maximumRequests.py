#!/usr/bin/python3
"""LeetCode Problem #1601 --> Maximum Number of Achievable Request Transfers"""
from collections import Counter
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0
        curr = [0 for i in range(n)]

        def backtrack(idx: int, req: int) -> None:
            nonlocal max_requests
            if idx >= len(requests):
                if len(Counter(curr)) == 1:
                    max_requests = max(max_requests, req)
                return

            a, b = requests[idx]
            if a != b:
                curr[a] -= 1
                curr[b] += 1

            backtrack(idx + 1, req + 1)

            if a != b:
                curr[a] += 1
                curr[b] -= 1

            backtrack(idx + 1, req)

        backtrack(0, 0)
        return max_requests
