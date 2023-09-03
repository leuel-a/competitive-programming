#!/usr/bin/python3
"""LeetCode Problem #773 --> Sliding Puzzle"""
from collections import deque
from typing import List, Tuple


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        for i in range(len(board)):
            for j, val in enumerate(board[i]):
                if val == 0:
                    initial_place = (i, j)
                    break
        visited = set([self.toTuple(board)])
        queue = deque([(board, initial_place, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        target = [
            [1, 2, 3],
            [4, 5, 0]
        ]

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < 2 and 0 <= col < 3

        while queue:
            curr_state, curr_place, moves = queue.popleft()

            if curr_state == target:
                return moves
            
            row, col = curr_place
            for rInc, cInc in directions:
                newR = row + rInc
                newC = col + cInc
                if inbound(newR, newC):
                    board_copy = [row[:] for row in curr_state]

                    board_copy[row][col], board_copy[newR][newC] = board_copy[newR][newC], board_copy[row][col]
                    if self.toTuple(board_copy) not in visited:
                        visited.add(self.toTuple(board_copy))
                        queue.append((board_copy, (newR, newC), moves + 1))
        return -1

    def toTuple(self, container: List[List[int]]) -> Tuple[Tuple[int]]:
        return tuple([tuple(row) for row in container])