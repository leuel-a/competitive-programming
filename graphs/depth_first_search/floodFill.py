#!/usr/bin/python3
"""LeetCode Problem #733 --> Flood Fill"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.source_color = image[sr][sc]

        def depth_first_search(node: list[int]) -> None:
            if node in visited:
                return

            row, col = node
            visited.add((row, col))
            image[row][col] = color
            for direction in directions:
                row_inc, col_inc = direction
                if in_bound(row + row_inc, col + col_inc) and self.source_color == image[row + row_inc][col + col_inc]:
                    depth_first_search((row + row_inc, col + col_inc))

        def in_bound(row: int, col: int) -> None:
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        depth_first_search((sr, sc))
        return image
