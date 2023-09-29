"""Leetcode Problem #677 --> Max Sum Pairs"""
from typing import List
from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.keys = set()


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.key_values = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        self.key_values[key] = val

        for char in key:
            idx = ord(char) - ord('a')

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.keys.add(key)
        curr.is_end = True

    def sum(self, prefix: str) -> int:
        curr = self.root

        for char in prefix:
            idx = ord(char) - ord('a')

            if curr.children[idx] is None:
                return 0
            curr = curr.children[idx]

        result = 0
        for key in curr.keys:
            result += self.key_values[key]
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
