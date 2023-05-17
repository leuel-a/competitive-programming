#!/usr/bin/python3
"""LeetCode Problem #684 --> Redundant Connection"""
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint_set = UnionFind(len(edges))

        curr = [0, 0]
        for a, b in edges:
            if disjoint_set.representative(a - 1) == disjoint_set.representative(b - 1):
                curr[0], curr[1] = a, b
                continue
            disjoint_set.union(a - 1, b - 1)
        return curr
