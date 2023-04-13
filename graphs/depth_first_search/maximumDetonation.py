#!/usr/bin/python3
"""LeetCode Problem #2101 --> Detonate the Maximum Bombs"""
from math import sqrt
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        visited, max_detonated = set(), 0
        graph = defaultdict(list)

        for i, bomb in enumerate(bombs):
            x1, y1, r1 = bomb
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    if sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= r1:
                        graph[i].append(j)

        def detonate_bombs(bomb: int) -> None:
            nonlocal count
            if bomb in visited:
                return

            count += 1
            visited.add(bomb)
            for val in graph[bomb]:
                detonate_bombs(val)

        for i in range(len(bombs)):
            count = 0
            visited.clear()
            detonate_bombs(i)
            max_detonated = max(max_detonated, count)
        return max_detonated

