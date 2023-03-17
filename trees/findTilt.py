#!/usr/bin/python3
"""LeetCode Problem #563 --> Binary Tree Tilt"""


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilts = []

        def findTiltHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = findTiltHelper(root.left)
            right = findTiltHelper(root.right)

            tilts.append(abs(left - right))
            return left + right + root.val
        findTiltHelper(root)
        return sum(tilts)
