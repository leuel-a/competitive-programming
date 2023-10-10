"""Leetcode Problem #652 --> Find Duplicate Subtrees"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashMap = {}
        result = []
        visited = set()

        def dfs(node: Optional[TreeNode], fromType: str = None):
            if not node:
                return 'L#' if fromType == 'L' else 'R#'

            left = dfs(node.left, 'L')
            right = dfs(node.right, 'R')

            curr = left + str(node.val) + right
            print(curr)
            if curr in hashMap and curr not in visited:
                result.append(node)
                visited.add(curr)
            hashMap[curr] = node
            return curr

        dfs(root)
        return result
