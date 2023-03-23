#!/usr/bin/python3
"""LeetCode Problem #1008 --> Construct Binary Search Tree from Preorder Traversal"""


class Solution:
    def bstFromPreorder(self, preorder) -> 'TreeNode':
        stack, temp = [], None
        root = TreeNode(preorder[0])

        stack.append(root)
        for val in preorder[1:]:
            while stack and stack[-1].val < val:
                temp = stack.pop()

            new_node = TreeNode(val)
            if temp:
                temp.right = new_node
                temp = None
            else:
                stack[-1].left = new_node
            stack.append(new_node)
        return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
