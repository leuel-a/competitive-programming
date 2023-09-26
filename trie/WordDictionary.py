"""Leetcode Problem #211 --> Design Add and Search Words Data Structure"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        curr.is_end = True

    def search(self, word: str) -> bool:
        return self.search_helper(0, self.root, word)

    def search_helper(self, idx: int, trieNode: TrieNode, word: str) -> bool:
        if idx == len(word):
            return trieNode.is_end

        char = word[idx]
        if char == '.':
            for i in range(26):
                if trieNode.children[i] and self.search_helper(idx + 1, trieNode.children[i], word):
                    return True
            return False
        else:
            child_idx = ord(char) - ord('a')
            if trieNode.children[child_idx]:
                return self.search_helper(idx + 1, trieNode.children[child_idx], word)
            return False
