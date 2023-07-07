#!/usr/bin/python3
"""LeetCode Problem #1722 --> Minimize Hamming Distance After Swap Operations"""
from typing import List
from collections import defaultdict


class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find_set(self, v: int) -> int:
        if self.parent[v] == v:
            return v

        # Path Compression
        p = self.find_set(self.parent[v])
        self.parent[v] = p
        return p

    def union_sets(self, a: int, b: int) -> bool:
        arep = self.find_set(a)
        brep = self.find_set(b)

        if arep == brep:
            return

        greater = arep if self.size[arep] >= self.size[brep] else brep
        smaller = brep if greater == arep else arep

        # Union them by size
        self.parent[smaller] = greater
        self.size[greater] += self.size[smaller]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uF = DSU(len(source))
        source_set = set(source)

        for a, b in allowedSwaps:
            uF.union_sets(a, b)

        groups = defaultdict(dict)
        for idx, val in enumerate(uF.parent):
            val = uF.find_set(val)
            if groups[val].get(source[idx]) == None:
                groups[val][source[idx]] = 1
            else:
                groups[val][source[idx]] += 1

        count = 0
        for idx, val in enumerate(target):
            if val not in source_set:
                count += 1
            else:
                idx_group = uF.find_set(idx)
                if val in groups[idx_group] and groups[idx_group][val] > 0:
                    groups[idx_group][val] -= 1
                else:
                    count += 1
        return count
