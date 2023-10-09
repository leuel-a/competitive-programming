"""Leetcode Problem #567 --> Permutation in String"""
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        s2_window_count = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_window_count[s2[i]] += 1

        if s1_count == s2_window_count:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            if s2_window_count[s2[i - 1]] == 1:
                del s2_window_count[s2[i - 1]]
            else:
                s2_window_count[s2[i - 1]] -= 1

            s2_window_count[s2[i + len(s1) - 1]] += 1
            if s1_count == s2_window_count:
                return True

        return False
