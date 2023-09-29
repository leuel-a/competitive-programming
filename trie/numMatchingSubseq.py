"""Leetcode Problem #792 --> Number of Matching Subsequences"""
from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        answer = 0
        starts = defaultdict(list)

        for word in words:
            starts[word[0]].append((0, word))
        
        for char in s:
            curr = starts[char]
            starts[char] = []
            
            for idx, word in curr:
                idx += 1

                if idx == len(word):
                    answer += 1
                else:
                    starts[word[idx]].append((idx, word))
        return answer
