#!/usr/bin/python3
"""LeetCode Problem #322 --> Coin Change"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def findMinCoins(curr: int) -> int:
            if curr == 0:
                return 0

            local_min = float('inf')
            for coin in coins:
                change = curr - coin
                if change in memo:
                    local_min = min(memo[change], local_min)
                elif change > -1:
                    local_min = min(findMinCoins(change), local_min)
            memo[curr] = 1 + local_min
            return memo[curr]
        val = findMinCoins(amount)
        return -1 if val == float('inf') else val
