#!/usr/bin/python3
"""LeetCode #853 --> Car Fleet"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        _t_p = []

        for ind, val in enumerate(position):
            t = (target - val) / speed[ind]
            _t_p.append((val, t))

        _t_p.sort(reverse=True)

        for elem in _t_p:
            while not stack or stack[-1][1] < elem[1]:
                stack.append(elem)
        return len(stack)
