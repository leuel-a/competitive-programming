#!/usr/bin/python3
"""LeetCode Problem #1584 --> Min Cost to Connect All Points"""
from heapq import heapify, heappop
from typing import Tuple, List


class DSU:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find_set(self, v: Tuple[int]) -> int:
        if v == self.parent[v]:
            return v

        parent = self.find_set(self.parent[v])
        self.parent[v] = parent
        return parent

    def union_sets(self, a: Tuple[int], b: Tuple[int]) -> None:
        arep = self.find_set(a)
        brep = self.find_set(b)

        if arep == brep:
            return

        greater = arep if self.size[arep] >= self.size[brep] else brep
        smaller = brep if greater == arep else arep

        self.parent[smaller] = greater
        self.size[greater] += self.size[smaller]

    def connected(self, a: List[int], b: List[int]) -> bool:
        return self.find_set(a) == self.find_set(b)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, seen = [], set()
        n = len(points)

        # GENERATE ALL THE EDGES OF THE MAXIMALLY CONNECTED GRAPH
        for i in range(len(points)):
            for j in range(len(points)):
                # CHECK ADDED FOR NOT DOUBLE ADDING OF EDGES
                if i == j or (i, j) in seen or (j, i) in seen:
                    continue
                a = points[i]
                b = points[j]
                dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
                edges.append([dist, i, j])
                seen.add((i, j))

        heapify(edges)
        UnionFind = DSU(n)

        min_cost, e = 0, 0
        while e < n - 1:
            dist, x, y = heappop(edges)
            if UnionFind.find_set(x) != UnionFind.find_set(y):
                min_cost += dist
                UnionFind.union_sets(x, y)
                e += 1
        return min_cost
