#!/usr/bin/python3
"""LeetCode #438 --> Find All Anagrams in a String"""
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        i = j = 0
        dict_s = {}
        p_dict = Counter(p)
        anagrams_index = []

        while j < len(s):
            if j - i + 1 > len(p):
                i += 1

            if j - i + 1 == len(p):
                if Counter(s[i:j+1]) == p_dict:
                    anagrams_index.append(i)
            j += 1
        return anagrams_index
