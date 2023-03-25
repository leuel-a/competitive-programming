#!/usr/bin/python3
"""LeetCode Problem #501 --> Find Mode in Binary Search Tree"""


class Solution:
    def findMode(self, root: 'TreeNode') -> list:
        _dict, _max = {}, float('-inf')

        def countNodes(root: 'TreeNode') -> None:
            nonlocal _max
            if not root:
                return

            countNodes(root.left)
            _dict[root.val] = _dict.get(root.val, 0) + 1

            if _max < _dict[root.val]:
                _max = _dict[root.val]

            countNodes(root.right)

        countNodes(root)

        modes = []
        for idx, val in _dict.items():
            if _max == val:
                modes.append(idx)
        return modes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
