#!/usr/bin/python3
"""LeetCode Problem #1971 --> Find if Path Exists"""
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.rep = {i: i for i in range(n)}
        self.size = [1 for _ in range(n)]

    def representative(self, x: int) -> int:
        parent = x
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while x != parent:
            prev = self.rep[x]
            self.rep[x] = parent
            x = prev
        return parent

    def union(self, x: int, y: int) -> None:
        xrep = self.representative(x)
        yrep = self.representative(y)

        if xrep == yrep:
            return

        greater = xrep if self.size[xrep] >= self.size[yrep] else yrep
        smaller = xrep if greater == yrep else yrep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]


    def connected(self, x: int, y: int) -> bool:
        return self.representative(x) == self.representative(y)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        disjoint_set = UnionFind(n)

        for a, b in edges:
            disjoint_set.union(a, b)
        return disjoint_set.connected(source, destination)
