#!/usr/bin/python3
""""""
from typing import List
from collections import deque


class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> int:
        graph = [[] for _ in range(K)]
        indegree = [0 for _ in range(K)]


        for idx in range(1, len(alien_dict)):
            j = 0
            prev, curr = alien_dict[idx - 1], alien_dict[idx]
            while j < min(len(prev), len(curr)):
                if prev[j] != curr[j]:
                    graph[ord(prev[j]) - 97].append(ord(curr[j]) - 97)
                    indegree[ord(curr[j]) - 97] += 1
                    break
                j += 1

        queue = deque()
        for idx, elem in enumerate(indegree):
            if elem == 0:
                queue.append(idx)

        order = []
        while queue:
            val = queue.popleft()
            order.append(chr(val + 97))

            for neighbour in graph[val]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return order
