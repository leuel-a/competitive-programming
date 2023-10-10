from typing import Optional, List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = defaultdict(lambda: float('-inf'))
        queue = deque([(root, 0)])
        last = -1

        while queue:
            node, level = queue.popleft()
            last = max(last, level)

            levels[level] = max(levels[level], node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        result = []
        for i in range(last + 1):
            result.append(levels[i])
        return result
