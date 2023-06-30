#!/usr/bin/python3
"""LeetCode Problem #1202 --> Smallest String With Swaps"""
from typing import List
from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find_set(self, v: int) -> int:
        if self.rep[v] == v:
            return v
        parent = self.find_set(self.rep[v])
        self.rep[v] = parent
        return parent

    def union_sets(self, a: int, b: int) -> None:
        arep = self.find_set(a)
        brep = self.find_set(b)

        if arep == brep:
            return

        greater = arep if self.size[arep] >= self.size[brep] else brep
        smaller = brep if greater == arep else arep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        unionFind = DSU(len(s))

        for a, b in pairs:
            unionFind.union_sets(a, b)

        groups = defaultdict(list)
        for i in range(len(s)):
            groups[unionFind.find_set(i)].append(s[i])

        for val in groups.values():
            val.sort(reverse=True)

        result = []
        for i in range(len(s)):
            result.append(groups[unionFind.find_set(i)].pop())
        print(result)
        return "".join(result)
