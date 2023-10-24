"""Leetcode Problem #49 --> Group Anagrams"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        MOD = pow(10, 9) + 7

        for word in strs:
            curr = 0
            for char in word:
                # This is a really neat way to do it since we need to have unique values for
                # each value character in the string --> More about advanced hashing
                curr += pow(27, ord(char) - ord('a') + 1, MOD)
            hashmap[curr].append(word)

        result = []
        for value in hashmap.values():
            result.append(value)
        return result
