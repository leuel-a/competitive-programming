#!/usr/bin/python3
"""LeetCode Problem #721 --> Accounts Merge"""
from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n) -> None:
        self.rep = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def representative(self, node: int) -> int:
        parent = node
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        # Path Compression
        while node != parent:
            prev = self.rep[node]
            self.rep[node] = parent
            node = prev
        return parent

    def union(self, x: int, y: int) -> None:
        xrep = self.representative(x)
        yrep = self.representative(y)

        greater = xrep if self.size[xrep] >= self.size[yrep] else yrep
        smaller = yrep if greater == xrep else xrep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]

    def connected(self, x: int, y: int) -> bool:
        return self.representative(x) == self.representative(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = DisjointSet(len(accounts))

        seen = {}
        for idx, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in seen:
                    unionFind.union(idx, seen[email])
                else:
                    seen[email] = idx
                    unionFind.size[idx] += 1

        result = defaultdict(set)
        for idx, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                rep = unionFind.representative(idx)
                result[rep].add(email)

        finalResult = []
        for key, val in result.items():
            finalResult.append([accounts[key][0]] + sorted(val))

        return finalResult
