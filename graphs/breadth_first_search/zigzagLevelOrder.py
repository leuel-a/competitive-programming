"""Leetcode Problem #"""
from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        levels = defaultdict(list)

        while queue:
            node, level = queue.popleft()

            levels[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        for level, nodes in levels.items():
            if level % 2 != 0:
                levels[level] = nodes[::-1]

        result = []
        for _, nodes in levels.items():
            result.append(nodes)
        return result
