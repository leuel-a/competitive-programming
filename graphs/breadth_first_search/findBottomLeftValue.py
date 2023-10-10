"""Leetcode Problem #513 --> Find Bottom Left Tree Value"""
from typing import Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        queue = deque([(root, 0)])
        last_level = -1

        while queue:
            node, level = queue.popleft()
            last_level = max(last_level, level)

            levels[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return levels[last_level][0]
