#!/usr/bin/python3
"""LeetCode Problem #1315 --> Sum of Nodes with Even-Valued Grandparent"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        path, _sum = [], 0

        def depth_first_search(node: TreeNode) -> None:
            nonlocal _sum
            if not node:
                return

            if len(path) >= 2 and path[len(path) - 2] % 2 == 0:
                _sum += node.val

            path.append(node.val)
            depth_first_search(node.left)
            depth_first_search(node.right)
            path.pop()

        depth_first_search(root)
        return _sum
