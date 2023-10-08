"""Leetcode Problem #662 --> Maximum Width of Binary Tree"""
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            _, first_idx = queue[0]

            for i in range(level_length):
                node, idx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx + 1))
            max_width = max(max_width, idx - first_idx + 1)

        return max_width
