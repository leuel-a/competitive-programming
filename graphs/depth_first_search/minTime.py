#!/usr/bin/python3
"""LeetCode Problem #1443 --> Minimum Time to Collect All Apples in a Tree"""
from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def collect_all_apples(node: int, time: int):
            visited.add(node)

            min_time = 0
            check_path = False
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found_apple, time_taken = collect_all_apples(neighbour, 0)
                    if found_apple:
                        min_time += time_taken
                        check_path = True

            if node == 0:
                return min_time

            time += min_time
            if hasApple[node] or check_path:
                return True, time + 2
            return False, time
        return collect_all_apples(0, 0)
