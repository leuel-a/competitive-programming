"""Leetcode Problem #787 --> Cheapest Flight Within K Stops"""
from typing import List
from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        distances = [float('inf') for _ in range(n)]
        distances[src] = 0

        queue = deque([(src, 0, 0)])
        while queue:
            node, count, dist = queue.popleft()

            if count > k:
                continue

            for nbr, w in graph[node]:
                distance = dist + w
                if distance < distances[nbr]:
                    distances[nbr] = distance
                    queue.append((nbr, count + 1, distance))
        return distances[dst] if distances[dst] < float('inf') else -1
