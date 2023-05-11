#!/usr/bin/python3
"""LeetCode Problem #2246 --> Longest Path With Different Adjacent Characters"""
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        visited = set()
        longest_path = float('-inf')
        graph = [[] for _ in range(len(parent))]

        for idx, val in enumerate(parent):
            if val != -1:
                graph[idx].append(val)
                graph[val].append(idx)

        def depth_first_search(node: int) -> int:
            nonlocal longest_path
            visited.add(node)

            c_bestchild = 0
            for neighbour in graph[node]:
                if neighbour not in visited:
                    val = depth_first_search(neighbour)
                    if s[neighbour] != s[node]:
                        longest_path = max(c_bestchild + 1 + val, longest_path)
                        c_bestchild = max(c_bestchild, val)
            return 1 + c_bestchild
        depth_first_search(0)
        return 1 if longest_path == float('-inf') else longest_path
