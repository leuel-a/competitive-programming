from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # to collect the nodes in each level
        verticalLevels = defaultdict(list)
        leftMin = rightMax = 0

        def DFS(node: Optional[TreeNode], level: int, depth: int) -> None:
            """Uses depth first search to calculate the vertical level traversal of the nodes in a tree"""
            nonlocal leftMin, rightMax
            if not node:
                return

            leftMin = min(leftMin, level)
            rightMax = max(rightMax, level)

            verticalLevels[level].append((depth, node.val))

            DFS(node.left, level - 1, depth + 1)
            DFS(node.right, level + 1, depth + 1)

        DFS(root, 0, 0)

        result = []
        for i in range(leftMin, rightMax + 1):
            currLevelNodes = []
            currLevel = sorted(verticalLevels[i])  # Sort
            for level, node in currLevel:
                currLevelNodes.append(node)
            result.append(currLevelNodes)
        return result
