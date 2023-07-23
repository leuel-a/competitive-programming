#!/usr/bin/python3
"""LeetCode Problem #815 --> Bus Routes"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Build a stop-to-routes mapping
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Initialize the queue for BFS
        queue = deque([(source, 0)])
        visited_routes = set()
        visited_stops = set([source])

        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses

            for route_idx in stop_to_routes[stop]:
                if route_idx not in visited_routes:
                    visited_routes.add(route_idx)
                    for next_stop in routes[route_idx]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses + 1))
        return -1
