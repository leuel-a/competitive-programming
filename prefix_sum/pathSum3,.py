"""Leetcode Problem #437 --> Path Sum III"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = {0: 1}
        count = 0

        def backtrack(root: Optional[TreeNode], _sum: int) -> None:
            nonlocal count

            if not root:
                return

            _sum += root.val
            if _sum - targetSum in prefix_sum:
                count += prefix_sum[_sum - targetSum]

            prefix_sum[_sum] = prefix_sum.get(_sum, 0) + 1

            backtrack(root.left, _sum)
            backtrack(root.right, _sum)

            prefix_sum[_sum] -= 1

        backtrack(root, 0)
        return count
