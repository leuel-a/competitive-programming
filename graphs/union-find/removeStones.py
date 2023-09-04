#!/usr/bin/python3
"""LeetCode Problem #947 --> Most Stones Removed with Same Row or Column"""
from typing import List


class DisJointSet:
    def __init__(self, n: int):
        self.rep = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def representative(self, node: int) -> int:
        parent = node
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != parent:
            prev = self.rep[node]
            self.rep[node] = parent
            node = prev
        return parent

    def union(self, a: int, b: int) -> None:
        arep = self.representative(a)
        brep = self.representative(b)

        if arep == brep:
            return

        greater = arep if self.size[arep] >= self.size[brep] else brep
        smaller = brep if greater == arep else arep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]

    def connected(self, a: str, b: str) -> bool:
        return self.representative(a) == self.representative(b)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        unionFind = DisJointSet(len(stones))

        for i in range(len(stones)):
            a, b = stones[i]
            for j in range(len(stones)):
                c, d = stones[j]

                if a == c or b == d:
                    unionFind.union(i, j)

        for i in range(len(stones)):
            unionFind.representative(i)
        return len(stones) - len(Counter(unionFind.rep)) if len(stones) > 1 else 0