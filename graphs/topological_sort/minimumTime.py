#!/usr/bin/python3
"""GeeksForGeeks Problem"""
from typing import List
from collections import deque



class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        
        for a, b in edges:
            graph[a -  1].append(b - 1)
            indegree[b - 1] += 1
            
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append((i, 1))
        
        minCompletion = [0 for _ in range(n)]
        while queue:
            val, time = queue.popleft()
            minCompletion[val] = time
            
            for neighbour in graph[val]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append((neighbour, time + 1))
        return ' '.join(str(val) for val in minCompletion)
