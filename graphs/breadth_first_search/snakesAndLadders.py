#!/usr/bin/python3
"""LeetCode Problem #909 --> Snakes and Ladders"""
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        value = 1
        dict_s = {}

        alternate = 0
        for i in range(n - 1, -1, -1):
            if alternate == 1:
                for j in range(n - 1, -1, -1):
                    dict_s[value] = (i, j)
                    value += 1
            else:
                for j in range(n):
                    dict_s[value] = (i, j)
                    value += 1
            alternate = 1 - alternate

        queue = deque([((n - 1, 0), 0, 1)])
        visited = set([(n - 1, 0)])
        while queue:
            (row, col), move, curr = queue.popleft()
            if curr == n ** 2:
                return move

            a = curr + 1
            b = min(curr + 6, n ** 2) + 1
            for aux in range(a, b):
                if dict_s[aux] not in visited:
                    visited.add(dict_s[aux])
                    row, col = dict_s[aux]
                    if board[row][col] != -1:
                        queue.append((dict_s[board[row][col]], move + 1, board[row][col]))
                    else:
                        queue.append((dict_s[aux], move + 1, aux))
        return -1
