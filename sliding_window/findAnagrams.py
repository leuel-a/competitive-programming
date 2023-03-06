#!/usr/bin/python3
"""LeetCode Problem #438 --> Find all Anagrams in a String"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        i, j = 0, 0
        total, p_dict = len(p), Counter(p)




sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
