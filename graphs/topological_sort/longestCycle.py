#!/usr/bin/python3
"""LeetCode Problem #2360 --> Longest Cycle in a Graph"""
from typing import List
from collections import defaultdict


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        color = [0 for _ in range(len(edges))]
        graph = [[] for _ in range(len(edges))]

        for idx, val in enumerate(edges):
            if val != -1:
                graph[idx].append(val)

        def dfs(node: int, path: int) -> None:
            nonlocal max_cycle
            if color[node] == 1:
                if node in seen_inpath:
                    max_cycle = max(max_cycle, path - last_seen[node])
                return False
            
            seen_inpath.add(node)
            color[node] = 1
            for neighbour in graph[node]:
                if color[neighbour] != 2:
                    if last_seen[neighbour] == 0:
                        last_seen[neighbour] = path + 1
                    if not dfs(neighbour, path + 1):
                        return False                    
            color[node] = 2
            return True

        max_cycle = -1
        seen_inpath = set()
        last_seen = defaultdict(int)
        for i in range(len(edges)):
            if color[i] == 0:
                seen_inpath.clear()
                last_seen[i] = 1
                dfs(i, 1)
        return max_cycle
