#!/usr/bin/python3
"""LeetCode Problem #1519 --> Number of Nodes in the Sub-Tree With The Same Label"""
from typing import List, Optional


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited, result = set(), [1 for _ in range(n)]

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def depth_first_search(node: int, descendants: List[int]) -> List[int]:
            visited.add(node)

            val = [0 for _ in range(26)]
            for neighbour in graph[node]:
                if neighbour not in visited:
                    neighbour_labels = depth_first_search(neighbour, [0 for _ in range(26)])
                    for i in range(26):
                        val [i] += neighbour_labels[i]
            result[node] += val[ord(labels[node]) - 97]
            val[ord(labels[node]) - 97] += 1
            return val
        depth_first_search(0, [0 for _ in range(26)])
        return result
