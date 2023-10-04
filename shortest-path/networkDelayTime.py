"""Leetcode Problem #743 --> Network Delay Time"""
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))  # Build the graph appropriately

        times = {i: float('inf') for i in range(1, n + 1)}
        times[k] = 1

        pq = [(0, k)]
        while pq:
            curr_dist, curr_node = heappop(pq)

            for weight, nxt_node in graph[curr_node]:
                if curr_dist + weight < times[nxt_node]:
                    times[nxt_node] = curr_dist + weight
                    heappush(pq, (times[nxt_node], nxt_node))
        result = max(times.values())
        return result if result != float('inf') else -1
