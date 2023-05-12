#!/usr/bin/python3
""""""
from typing import List
from collections import defaultdict, deque


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = set()
        queue = deque()
        graph = defaultdict(list)

        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
            nums.add(i)
            nums.add(j)

        visited = set()
        for num in nums:
            if len(graph[num]) == 1:
                queue.append(num)
                visited.add(num)
                break

        result = []
        while queue:
            node = queue.popleft()

            for val in graph[node]:
                if val not in visited:
                    queue.append(val)
                    visited.add(val)
            result.append(node)
        return result


