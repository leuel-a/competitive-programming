#!/usr/bin/python3
"""LeetCode Problem #1391 --> Check if There is a Valid Path in a Grid"""
from typing import List
from itertools import product


class UnionFind:
    def __init__(self, nodes: List[tuple]) -> None:
        self.rep = {node: node for node in nodes}
        self.size = defaultdict(lambda : 1)

    def representative(self, node: tuple) -> int:
        parent = node
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != parent:
            prev = self.rep[node]
            self.rep[node] = parent
            node = prev
        return parent

    def union(self, x: tuple, y: tuple) -> None:
        xrep = self.representative(x)
        yrep = self.representative(y)

        if xrep == yrep:
            return

        greater = xrep if self.size[xrep] >= self.size[yrep] else yrep
        smaller = xrep if greater == yrep else yrep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]


    def connected(self, x: tuple, y: tuple) -> bool:
        return self.representative(x) == self.representative(y)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        uF = UnionFind(product(range(len(grid)), range(len(grid[0]))))
        directions = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                key = grid[row][col]

                for row_inc, col_inc in directions[key]:
                    new_row, new_col = row + row_inc, col + col_inc

                    if in_bound(new_row, new_col):
                        val = grid[new_row][new_col]
                        if (-row_inc, -col_inc) in directions[val]:
                            uF.union((new_row, new_col), (row, col))

        return uF.connected((0, 0), (len(grid) - 1, len(grid[0]) - 1))

