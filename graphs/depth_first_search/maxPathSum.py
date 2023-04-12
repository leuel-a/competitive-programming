#!/usr/bin/python3
"""LeetCode Problem 124 --> Binary Tree Maximum Path Sum"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: 'TreeNode') -> int:
        max_path = float('-inf')

        def depth_first_search(root: 'TreeNode') -> int:
            nonlocal max_path
            if not root:
                return 0

            left = depth_first_search(root.left)
            right = depth_first_search(root.right)
            max_path = max(max_path, left + right + root.val, left + root.val, right + root.val, root.val)
            return max(left + root.val, right + root.val, root.val)

        depth_first_search(root)
        return max_path
