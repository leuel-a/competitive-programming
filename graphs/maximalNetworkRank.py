#!/usr/bin/python3
"""LeetCode Problem #1615 --> Maximal Network Rank"""
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        adj_list = defaultdict(set)

        for road in roads:
            adj_list[road[0]].add(road[1])
            adj_list[road[1]].add(road[0])

        _max = 0
        for key, val in adj_list.items():
            for i, elem in adj_list.items():
                if i != key:
                    if key in elem:
                        _max = max(_max, len(val) + len(elem) - 1)
                    else:
                        _max = max(_max, len(val) + len(elem))
        return _max
