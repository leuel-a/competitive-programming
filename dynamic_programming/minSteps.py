"""Leetcode Problem #650 --> 2 Keys Keyboard"""
from typing import List


class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        
        def dp(curr: int, aux: int, count: int) -> int:
            state = f'{curr}, {aux}'

            # Handle the Base Cases Here
            if state in memo:
                return memo[state]
            
            if len(curr) == n:
                return count
            
            if len(curr) > n:
                return float('inf')

            # Copy the current values if possible and is effcient
            copy = float('inf') if len(curr) <= len(aux) else dp(curr, curr, count + 1)

            # Paste the current values if possible
            paste = float('inf') if aux == '' else dp(curr + aux, aux, count + 1)

            memo[state] = min(copy, paste)
            return memo[state]
        return dp('A', '', 0)
            
