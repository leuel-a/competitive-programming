#!/usr/bin/python3
"""LeetCode Problem #818 --> Race Car"""
from collections import deque
from typing import Optional, List, Tuple, Deque


class Solution:
    def racecar(self, target: int) -> int:
        visited = set()
        queue = deque()
        length = 0

        queue.append((0, 1, 0))
        visited.add((0, 1))
        while queue:
            location, speed, level = queue.popleft()
            if location == target:
                return level

            # IF WE ACCELERATE THE CAR
            if (location + speed, speed * 2) not in visited:
                queue.append((location + speed, speed * 2, level + 1))
                visited.add((location + speed, speed * 2))

            # IF WE CHOOSE TO DECELERATE
            if (location, 1 if speed < 0 else -1) not in visited:
                queue.append((location, 1 if speed < 0 else -1, level + 1))
                visited.add((location, 1 if speed < 0 else -1))
        return -1
