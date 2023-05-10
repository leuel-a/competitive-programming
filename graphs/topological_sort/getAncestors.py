#!/usr/bin/python3
"""LeetCode Problem #2192 --> All Ancestors of a Node in a Directed Acyclic Graph"""
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = [[] for _ in range(n)]
        ancestors = [set() for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                ancestors[neighbour].update(ancestors[node])
                ancestors[neighbour].add(node)
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return [list(sorted(val)) for val in ancestors]

