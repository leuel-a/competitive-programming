#!/usr/bin/python3
"""LeetCode Problem #797 --> All Paths From Source to Target"""
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        adj_list = defaultdict(list)
        possible_paths = []

        for idx, elem in enumerate(graph):
            adj_list[idx].extend(elem)

        def depth_first_search(node: int, curr: list[int]) -> None:
            if node == len(graph) - 1:
                possible_paths.append(curr.copy())
                return

            for val in graph[node]:
                curr.append(val)
                depth_first_search(val, curr)
                curr.pop()

        depth_first_search(0, [0])
        return possible_paths
