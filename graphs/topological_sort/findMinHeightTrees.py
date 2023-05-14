#!/usr/bin/python3
"""LeetCode Problem #310 --> Minimum Height Trees"""
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            # Increment the indegree of the nodes
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        min_height_roots = []
        while queue:
            min_height_roots.clear()
            size = len(queue)

            for i in range(size):
                val = queue.popleft()
                min_height_roots.append(val)
                for neighbour in graph[val]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 1:
                        queue.append(neighbour)
        return min_height_roots if n > 1 else [0]
