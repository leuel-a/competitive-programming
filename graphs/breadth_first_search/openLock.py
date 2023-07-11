#!/usr/bin/python3
"""LeetCode Problem --> #752 Open the Lock"""
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        initial_state = [0, 0, 0, 0]
        queue = deque([(initial_state, 0)])
        visited = set([(0, 0, 0, 0)])

        while queue:
            state, moves = queue.popleft()

            if ''.join(map(str, state)) in deadends:
                continue

            if ''.join(map(str, state)) == target:
                return moves

            for i in range(4):
                curr = state[i]

                choice_one = state[:i] + [curr + 1 if curr + 1 < 10 else 0] + state[i+1:]
                choice_two = state[:i] + [curr - 1 if curr - 1 > -1 else 9] + state[i+1:]

                if tuple(choice_one) not in visited:
                    queue.append((choice_one, moves + 1))
                    visited.add(tuple(choice_one))

                if tuple(choice_two) not in visited:
                    queue.append((choice_two, moves + 1))
                    visited.add(tuple(choice_two))
        return -1
