#!/usr/bin/python3
"""LeetCode Problem #1462 --> Course Schedule IV"""
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        p = [set() for _ in range(numCourses)]
        while queue:
            val = queue.popleft()

            for neighbour in graph[val]:
                indegree[neighbour] -= 1
                p[neighbour].add(val)
                p[neighbour].update(p[val])

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        result = []
        for pre, course in queries:
            result.append(True if pre in p[course] else False)
        return result
