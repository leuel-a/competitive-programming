#!/usr/bin/python3
"""LeetCode Problem #886 --> Possible Bipartiton"""
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)

        for fr, to in dislikes:
            graph[fr].append(to)
            graph[to].append(fr)

        color = [-1 for i in range(n)]

        def depth_first_search(node: int) -> bool:
            for val in graph[node]:
                if color[val - 1] == -1:
                    color[val - 1] = 1 - color[node - 1]
                    depth_first_search(val)
                else:
                    if color[val - 1] == color[node - 1]:
                        return False
            return True


        for node in graph:
            if color[node - 1] == -1:
                color[node - 1] = 0
            if not depth_first_search(node):
                return False
        return True
