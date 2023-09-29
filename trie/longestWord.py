"""Leetcode Problem #720 --> Longest Word in Dictionary"""
from typing import List


class TrieNode:
    def __init__(self):
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
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)

        root = trie.root
        word_starts = []
        for i in range(26):
            if root.children[i] is not None:
                char = chr(i + ord('a'))
                word_starts.append((root.children[i], char))

        def count_childs(node: TrieNode) -> int:
            count = 0

            for i in range(26):
                if node.children[i] is not None:
                    count += 1
            return count

        def dfs(node: TrieNode, string: str) -> str:
            if node.is_end == False:
                return ""

            if count_childs(node) == 0:
                return string

            local = string
            for i in range(26):
                if node.children[i] is not None:
                    char = chr(i + ord('a'))
                    result = dfs(node.children[i], string + char)
                    if len(result) > len(local):
                        local = result
                    elif len(result) == len(local) and result < local:
                        local = result
            return local

        max_ = ""
        for start, char in word_starts:
            result = dfs(start, char)
            if len(result) > len(max_):
                max_ = result
            elif len(result) == len(max_) and result < max_:
                max_ = result
        return max_
