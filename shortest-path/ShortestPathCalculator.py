"""Leetcode Problem #2642 --> Design Graph With Shortest Path Calculator"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.size = n
        self.graph = defaultdict(list)

        # Building the graph
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf') for _ in range(self.size)]
        distances[node1] = 0

        heap = [(0, node1)]
        while heap:
            dist, node = heappop(heap)

            if distances[node] < dist:
                continue

            for neighbour, weight in self.graph[node]:
                distance = dist + weight
                if distances[neighbour] > distance:
                    distances[neighbour] = distance
                    heappush(heap, (distance, neighbour))
        return -1 if distances[node2] == float('inf') else distances[node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
