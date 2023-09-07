#!/usr/bin/python3
"""LeetCode Problem #1754 --> Largest Merge Of Two Strings"""
from typing import List, Tuple


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        w1, w2 = 0, 0
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1] > word2[w2]:
                merge += word1[w1]
                w1 += 1
            elif word1[w1] < word2[w2]:
                merge += word2[w2]
                w2 += 1
            else:
                first, second = w1 + 1, w2 + 1
                while first < len(word1) and second < len(word2):
                    if word1[first] > word2[second]:
                        merge += word1[w1]
                        w1 += 1
                        break
                    elif word1[first] < word2[second]:
                        merge += word2[w2]
                        w2 += 1
                        break
                    first += 1
                    second += 1
                else:
                    if first < len(word1) and second == len(word2):
                        merge += word1[w1]
                        w1 += 1
                    else:
                        merge += word2[w2]
                        w2 += 1
                        
        while w1 < len(word1):
            merge += word1[w1]
            w1 += 1
        while w2 < len(word2):
            merge += word2[w2]
            w2 += 1
        return merge