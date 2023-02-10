#!/usr/bin/python3
"""Defines the Solution Class"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j, max_vowels, count_vowels = 0, 0, 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        while j < len(s):
            if s[j] in vowels:
                count_vowels += 1
            while j - i + 1 > k:
                if s[i] in vowels:
                    count_vowels -= 1
                i += 1
            j += 1
            max_vowels = max(max_vowels, count_vowels)
        return max_vowels
