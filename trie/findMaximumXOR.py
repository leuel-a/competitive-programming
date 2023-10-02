"""Leetcode Problem #421 --> Maximum XOR of Two Numbers in an Array"""
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            tmp = max_xor | (1 << i)
            
            for prefix in prefixes:
                if tmp ^ prefix in prefixes:
                    max_xor = tmp
                    break

        return max_xor