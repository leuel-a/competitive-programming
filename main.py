"""Practice code"""
from typing import List
from collections import defaultdict, deque, Counter


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a new node into the trie"""
        curr = self.root

        for char in word:
            idx = ord(char) - 97

            # add the new character into your children if it does
            # not exist in your children in the first place
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        # Set the end node here because to search a word we will
        # use it later on
        curr.is_end = True

    def search(self, word: str) -> bool:
        """Searches for a word in a trie"""
        curr = self.root
        
        for char in word:
            idx = ord(char) - 97

            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """Checks if a prefix exists in a trie"""
        curr = self.root

        for char in prefix:
            idx = ord(char) - 97

            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
