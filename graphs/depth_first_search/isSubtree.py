"""Leetcode Problem #572 --> Subtree of Another Tree"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRootStr = ''
        foundMatch = False

        def dfs(node: Optional[TreeNode], flag: bool) -> str:
            nonlocal foundMatch
            if not node:
                return 'L#' if flag else 'R#'

            left = dfs(node.left, True)
            right = dfs(node.right, False)

            curr = left + right + str(node.val)
            print()
            if subRootStr and curr == subRootStr:
                print(curr, '||', subRootStr)
                foundMatch = True

            return curr
        subRootStr = dfs(subRoot, False)
        _ = dfs(root, False)
        return foundMatch
