#!/usr/bin/python3
"""LeetCode Problem #2492 --> Minimum Score of a Path Between Two Citites"""
from typing import List


class DisJointSet:
    def __init__(self, n: int) -> None:
        self.rep = [i for i in range(n)]
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unionFind = DisJointSet(n)
        min_path = float('inf')

        for a, b, length in roads:
            unionFind.union(a - 1, b - 1)

        # Task is to iterate over the groups and find the minimum of
        # the group in the the same group of 1 or n
        for a, b, length in roads:
            if unionFind.connected(a - 1, 0):
                min_path = min(min_path, length)
        return min_path

        
