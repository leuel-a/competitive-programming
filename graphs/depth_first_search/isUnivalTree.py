"""Leetcode Problem #965 --> Univalued Binary Tree"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        nodes = set()

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            nodes.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(nodes) == 1
