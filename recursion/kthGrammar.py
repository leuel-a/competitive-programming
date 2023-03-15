#!/usr/bin/python3
"""LeetCode #779 --> K-th Symbol in Grammar"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        _len = pow(2, n - 1)
        if k > (_len / 2):
            return 1 - self.kthGrammar(n - 1, k - _len // 2)
        return self.kthGrammar(n - 1, k)
