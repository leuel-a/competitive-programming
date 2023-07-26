#!/usr/bin/python3
"""LeetCode Problem #714 --> Best Time to Buy and Sell Stock with Transaction Fee"""
from typing import List
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def maximizeProfit(idx: int, bought: bool) -> int:
            # Base Case
            if idx >= len(prices):
                return 0

            if bought:
                return max(
                    maximizeProfit(idx + 1, False) + prices[idx] - fee,
                    maximizeProfit(idx + 1, bought)
                )

            return max(
                maximizeProfit(idx+1, True) - prices[idx],
                maximizeProfit(idx+1, bought)
            )
        return maximizeProfit(0, False)
