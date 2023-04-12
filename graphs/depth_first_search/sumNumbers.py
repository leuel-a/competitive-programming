#!/usr/bin/python3
"""LeetCode Problem #129 --> Sum Root to Leaf Numbers"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> int:
        nums = []

        def depth_first_search(root: 'TreeNode', curr: list[int]) -> None:
            if not root:
                return

            if not root.left and not root.right:
                curr.append(root.val)
                if len(curr) > 0:
                    nums.append(int(''.join(str(val) for val in curr)))
                curr.pop()
                return

            curr.append(root.val)
            depth_first_search(root.left, curr)
            depth_first_search(root.right, curr)
            curr.pop()
        depth_first_search(root, [])

        sumNumbers = 0
        for val in nums:
            sumNumbers += val
        return sumNumbers

