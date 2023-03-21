#!/usr/bin/python3
"""LeetCode #235 --> Lowest Common Ancestor"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val:
            return root
        if q.val <= root.val <= p.val:
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)
