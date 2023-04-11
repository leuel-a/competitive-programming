#!/usr/bin/python3
"""LeetCode Problem #547 --> Number of Provinces"""
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = set()
        graph = defaultdict(list)

        for i, val in enumerate(isConnected):
            for j, elem in enumerate(val):
                if i != j and elem == 1:
                    graph[i + 1].append(j + 1)

        def dfs_visit(i: int) -> None:
            nonlocal number_of_province

            visited.add(i)
            for neighbour in graph[i]:
                if neighbour not in visited:
                    number_of_province -= 1
                    dfs_visit(neighbour)


        number_of_province = len(isConnected)
        for i in range(1, len(isConnected) + 1):
            dfs_visit(i)

        return number_of_province
