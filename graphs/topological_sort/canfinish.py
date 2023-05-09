#!/usr/bin/python3
"""LeetCode Problem #207 --> Course Schedule"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        color = [0 for j in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        def topSort(pre: int) -> bool:
            if color[pre] == 1:
                return False

            color[pre] = 1
            for course in graph[pre]:
                if color[course] != 2:
                    if not topSort(course):
                        return False
            color[pre] = 2
            return True

        for i in range(numCourses):
            if color[i] == 0:
                if not topSort(i):
                    return False
        return True
