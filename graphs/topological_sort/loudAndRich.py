#!/usr/bib/python3
"""LeetCode Problem #851 --> Loud And Rich"""
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for _ in range(len(quiet))]

        for a, b in richer:
            graph[b].append(a)

        def depth_first_search(node: int) -> int:
            stack = [node]

            _min = node
            while stack:
                node = stack.pop()
                visited.add(node)

                for val in graph[node]:
                    if val not in visited:
                        _min = _min if quiet[_min] < quiet[val] else val
                        stack.append(val)
            return _min

        visited = set()
        answer = [0 for i in range(len(quiet))]
        for x in range(len(quiet)):
            if x not in visited:
                y = depth_first_search(x)
                answer[x] = y
                visited.clear()
        return answer

