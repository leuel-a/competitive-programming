"""Leetcode Problem #113 --> Path Sum II"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []

        def dfs(node: Optional[TreeNode], curr: List[int]) -> None:
            # If there is no node in the graph
            if not node:
                return None

            # Handle Base Cases Here

            curr.append(node.val)
            # if sum(curr) > targetSum:
            #     curr.pop()
            #     return None

            if not node.left and not node.right:
                if sum(curr) == targetSum:
                    all_paths.append(curr[:])
                    print(all_paths)
                curr.pop()
                return None

            dfs(node.left, curr)
            dfs(node.right, curr)

            curr.pop()
        dfs(root, [])
        return all_paths
