#!/usr/bin/python3
"""LeetCode Problem #559 --> Maximum Depth of N-ary Tree"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = float('-inf')
        visited = set()

        def depth_first_search(root: 'Node', depth: int) -> None:
            nonlocal max_depth
            if not root:
                max_depth = 0
                return

            visited.add(root)
            if len(root.children) == 0:
                max_depth = max(max_depth, depth + 1)
                return

            for child in root.children:
                depth_first_search(child, depth + 1)

        depth_first_search(root, 0)
        return max_depth
