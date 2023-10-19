"""Leetcode Problem #872 --> Leaf-Similar Trees"""""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1Leaves, root2Leaves = [], []

        flag = False

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal flag
            if not node:
                return

            if not node.left and not node.right:
                if flag:
                    root1Leaves.append(node.val)
                else:
                    root2Leaves.append(node.valw)
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root1)
        flag = True
        dfs(root2)

        if len(root1Leaves) != len(root2Leaves):
            return False

        for idx, val in enumerate(root1Leaves):
            if root2Leaves[idx] != val:
                return False
        return True
