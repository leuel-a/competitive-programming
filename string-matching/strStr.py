"""Leetcode Problem #28 --> Find the Index of the First Occurrence in a String"""
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def rabin_karp(text, pattern):
            # If the pattern's length is greater than the text's length, return -1
            if len(pattern) > len(text):
                return -1

            # Base for the rolling hash function
            base = 27

            # Modulus for preventing overflow
            modulus = 101

            # Length of the pattern
            m = len(pattern)

            # Length of the text
            n = len(text)

            # Hash values initialization
            pattern_hash = 0
            text_hash = 0

            # Compute the hash value for the pattern and first window of text
            for i in range(m):
                pattern_hash = (base * pattern_hash +
                                ord(pattern[i])) % modulus
                text_hash = (base * text_hash + ord(text[i])) % modulus

            # Traverse the text
            for s in range(n - m + 1):
                # If the hash values match, check character by character
                if pattern_hash == text_hash:
                    if text[s:s + m] == pattern:
                        return s  # Found a match at index s

                # If not at the end, compute the hash value for the next window
                if s < n - m:
                    text_hash = (
                        text_hash - ord(text[s]) * (base**(m - 1))) % modulus
                    text_hash = (text_hash * base + ord(text[s + m])) % modulus
                    # Handle negative hash values
                    text_hash = (text_hash + modulus) % modulus

            return -1  # Pattern not found in the text

        return rabin_karp(haystack, needle)
