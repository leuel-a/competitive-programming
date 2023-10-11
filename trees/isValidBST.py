"""Leetcode Problem #98 --> Validate Binary Search Tree"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN = float('-inf')
        MAX = float('inf')

        def helper(node: Optional[TreeNode], left: int, right: int) -> bool:
            if not node:
                return True

            if left > node.val or right < node.val:
                return False
            return helper(node.left, left, node.val - 1) and helper(node.right, node.val + 1, right)

        return helper(root.left, MIN, root.val - 1) and helper(root.right, root.val + 1, MAX)
