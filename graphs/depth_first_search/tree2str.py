#!/usr/bin/python3
"""LeetCode Problem #606 --> Construct String from Binary Tree """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: 'TreeNode') -> str:
        if not root:
            return ""

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left == "" and right == "":
            return f'{root.val}'
        elif left != "" and right == "":
            return f'{root.val}({left})'
        return f'{root.val}({left})({right})'
