"""Leetcode Problem #515 --> Find Largest Value in Each Tree Row"""
from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([(root, 0)])
        levels = defaultdict(lambda: float('-inf'))

        last = 0
        while queue:
            node, level = queue.popleft()

            levels[level] = max(levels[level], node.val)
            last = level

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        result = []
        for i in range(last + 1):
            result.append(levels[i])
        return result
