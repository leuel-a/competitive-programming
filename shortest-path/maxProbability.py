"""Leetcode Problem #1514 --> Path with Maximum Probability"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]

        # Build the graph
        for idx, (a, b) in enumerate(edges):
            graph[a].append((succProb[idx], b))
            graph[b].append((succProb[idx], a))

        max_probability = [0 for _ in range(n)]
        # This is to ensure that you can reach the start node from this current start node
        max_probability[start_node] = 1

        pq = [(-1, start_node)]
        while pq:
            curr_prob, curr_node = heappop(pq)

            if curr_node == end_node:
                return -curr_prob

            for path_prob, nxt_node in graph[curr_node]:
                if -curr_prob * path_prob > max_probability[nxt_node]:
                    max_probability[nxt_node] = -curr_prob * path_prob
                    heappush(pq, (-max_probability[nxt_node], nxt_node))
        return 0.0
