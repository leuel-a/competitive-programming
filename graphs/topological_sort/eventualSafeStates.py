#!/usr/bin/python3
"""LeetCode Problem #802 --> Find Eventual Safe States"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for i in range(len(graph))]
        
        def topSort(node: int) -> bool:
            if color[node] == 1:
                return False

            color[node] = 1
            for neigh in graph[node]:
                if color[neigh] != 2:
                    if not topSort(neigh):
                        return False

            color[node] = 2
            return True
        
        safe_nodes = []
        for i in range(len(graph)):
            if color != 0:
                if topSort(i):
                    safe_nodes.append(i)
        return safe_nodes
