#!/usr/bin/python3
"""LeetCode Problem #529 --> Minesweeper"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def check_mines(row: int, col: int) -> int:
            count = 0
            for row_inc, col_inc in directions:
                new_row, new_col = row + row_inc, col + col_inc
                if in_bound(new_row, new_col) and board[new_row][new_col] == 'M':
                    count += 1
            return count

        def depth_first_search(row: int, col: int) -> None:
            visited.add((row, col))

            count = check_mines(row, col)
            if count == 0:
                board[row][col] = 'B'
                for row_inc, col_inc in directions:
                    new_row, new_col = row + row_inc, col + col_inc
                    if in_bound(new_row, new_col) and board[new_row][new_col] == 'E':
                        depth_first_search(new_row, new_col)
            else:
                board[row][col] = str(count)

        visited = set()
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            depth_first_search(click[0], click[1])
        return board
