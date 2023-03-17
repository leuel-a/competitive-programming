#!/usr/bin/python3
"""LeetCode Problem #199 --> Binary Tree Right Side View"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView, dict_s = [], {}

        def rightSideViewHelper(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return

            if level not in dict_s.keys():
                rightView.append(root.val)
                dict_s[level] = root.val
            
            if root.right:
                rightSideViewHelper(root.right, level + 1)
            if root.left:
                rightSideViewHelper(root.left, level + 1)
        rightSideViewHelper(root, 0)
        return rightView
