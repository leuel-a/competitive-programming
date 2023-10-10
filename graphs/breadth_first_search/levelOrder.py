"""Leetcode Problem #429 --> N-ary Tree Level Order Traversal"""
from collections import defaultdict, deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        levels = defaultdict(list)
        queue = deque([(root, 0)])
        last = -1

        while queue:
            node, level = queue.popleft()
            last = max(last, level)

            levels[level].append(node.val)

            for nbr in node.children:
                queue.append((nbr, level + 1))

        result = []
        for i in range(last + 1):
            result.append(levels[i])
        return result
