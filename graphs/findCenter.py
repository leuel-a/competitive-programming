#!/usr/bin/python3
"""LeetCode Problem #1791 --> Find Center of Star Graph"""
from collections import defaultdict


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        adjacency_list = defaultdict(list)

        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        for key, val in adjacency_list.items():
            if len(val) == len(edges):
                return val
