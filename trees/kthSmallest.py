"""Leetcode Problem #230 --> Kth Smallest in a BST"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node: Optional[TreeNode]):
            if not node:
                return []

            left = inorder(node.left)
            right = inorder(node.right)

            return left + [node.val] + right
        inorderList = inorder(root)
        return inorderList[k-1]
