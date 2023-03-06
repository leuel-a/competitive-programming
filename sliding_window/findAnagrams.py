#!/usr/bin/python3
"""LeetCode Problem #438 --> Find all Anagrams in a String"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0, 0
        total, dict_s = 0, {}
        anagrams_index = []

        while j < len(s):
            if s[j] not in dict_s:
                dict_s[s[j]] = 1
                total += 1

                while total > len(p):
                    dict_s[s[i]] -= 1
                    
                    if dict_s[s[i]] == 0:
                        del dict_s[s[i]]
                        i += 1
                        total -= 1

                if total == len(p):
                    anagrams_index.append(i)

                j += 1
        return anagrams_index
