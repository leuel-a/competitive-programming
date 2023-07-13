#!/usr/bin/python3
"""LeetCode Problem #337 --> House Robber III"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]):
        node_map = {}
        self.traverse(root, node_map)
        return node_map[root]

    def traverse(self, root, node_map):
        if root is None:
            return
        if root.left is None and root.right is None:
            node_map[root] = root.val
            return
        count_root = 0
        x_root = 0
        if root.left is not None and root.left not in node_map:
            self.traverse(root.left, node_map)
            x_root += node_map[root.left]
            if root.left.left is not None:
                count_root += node_map[root.left.left]
            if root.left.right is not None:
                count_root += node_map[root.left.right]
        if root.right is not None and root.right not in node_map:
            self.traverse(root.right, node_map)
            x_root += node_map[root.right]
            if root.right.left is not None:
                count_root += node_map[root.right.left]
            if root.right.right is not None:
                count_root += node_map[root.right.right]
        node_map[root] = max(x_root, count_root + root.val)
