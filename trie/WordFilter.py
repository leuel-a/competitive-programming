"""Leetcode Problem #745 --> Prefix and Suffix Search"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.suffixes = defaultdict(lambda: -1)


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for idx, word in enumerate(words):
            self.insert(idx, word)  # Add the words to the dictionary

    def insert(self, index: int, word: str) -> None:
        curr = self.root

        for k, char in enumerate(word):
            j = ord(char) - ord('a')

            if curr.children[j] is None:
                curr.children[j] = TrieNode()
            curr = curr.children[j]

            for i in range(len(word)):
                curr.suffixes[word[i:]] = index
        curr.is_end = True

    def f(self, pref: str, suff: str) -> int:
        curr = self.root

        for char in pref:
            i = ord(char) - ord('a')

            if curr.children[i] is None:
                return -1
            curr = curr.children[i]

        found = False
        aux = None

        for word in curr.suffixes.keys():
            if word == suff:
                return curr.suffixes[word]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
