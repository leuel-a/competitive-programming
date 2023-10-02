"""Leetcode Problem #2416 --> Sum of Prefix Scores of Strings"""
from typing import List


class TrieNode:
    def __init__(self):
        self.count = 0
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.count += 1
        curr.is_end = True
    
    def get_counts(self, word: str) -> None:
        curr_count = 0
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')

            curr = curr.children[idx]
            curr_count += curr.count
        return curr_count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        result = []

        for word in words:
            trie.insert(word)

        for word in words:
            result.append(trie.get_counts(word))
        return result
        