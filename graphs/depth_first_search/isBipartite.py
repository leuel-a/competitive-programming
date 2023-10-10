"""Leetcode Problem #785 --> Is Graph Bipartite?"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for _ in range(n)]

        def dfs(node: int, nxt_color: int) -> bool:

            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = nxt_color
                    if not dfs(neighbour, 1 - nxt_color):
                        return False
                else:
                    if color[neighbour] != nxt_color:
                        return False
            return True

        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i, 1):
                    return False
        return True
