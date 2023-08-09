#!/usr/bin/python3
"""Leetcode Problem #1993 --> Operations on Tree"""
from collections import deque
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = [[] for _ in range(len(parent))]
        self.ancestors = [[] for _ in range(len(parent))]
        self.locked = {}

        # Build the initial graph
        for idx, node in enumerate(parent):
            if idx == 0:
                continue
            self.graph[node].append(idx)
            self.graph[idx].append(node)

        # Build the ancestors array
        # This will simplify the redundant operations that
        # you are going to do because that will take your time
        visited = set([0])
        queue = deque([(0, [])])

        while queue:
            node, ancestors = queue.popleft()

            self.ancestors[node].extend(ancestors)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, ancestors + [node]))


    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        # Check if the node is already unlocked
        if num not in self.locked:
            return False

        # Check if the node is not locked by the current user
        if self.locked[num] != user:
            return False

        del self.locked[num]
        return True


    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        hasNoAncestorLocked = True
        for val in self.ancestors[num]:
            if val in self.locked:
                hasNoAncestorLocked = False

        if not hasNoAncestorLocked:
            return False

        def depth_first_search(node: int) -> None:
            visited.add(node)
            if node in self.locked:
                nodesToUnlock.append(node)

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    depth_first_search(neighbour)

        visited = set([num])
        nodesToUnlock = []
        for node in self.graph[num]:
            if node not in self.ancestors[num]:
                depth_first_search(node)

        if len(nodesToUnlock) == 0:
            return False

        for node in nodesToUnlock:
            del self.locked[node]
        self.locked[num] = user
        return True
