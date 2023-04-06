#!/usr/bin/python3
"""LeetCode Problem #1557 --> Minimum Number of Verticies to Reach All Nodes"""
from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        count_array = [0] * n

        for edge in edges:
            count_array[edge[1]] += 1

        res = []
        for i, val in enumerate(count_array):
            if val == 0:
                res.append(i)
        return res
