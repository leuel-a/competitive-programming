#!/usr/bin/python3
"""CodeNinja Problem --> Parallel Courses"""
from typing import List
from collections import deque

def parallelCourses(N, prerequisites: List[int]):
    _min_semester, order = 0, []

    indegree = [0 for _ in range(N)]
    graph = [[] for _ in range(N)]
    for a, b in prerequisites:
        graph[a - 1].append(b - 1)
        indegree[b - 1] += 1

    queue = deque()
    visited = set()
    for i in range(N):
        if indegree[i] == 0:
            queue.append((i, 1))
            visited.add(i)

    while queue:
        node, semester = queue.popleft()
        order.append(node)
        _min_semester = semester

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append((neighbour, semester + 1))
    return -1 if len(order) != N else _min_semester
