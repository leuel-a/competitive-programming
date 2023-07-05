#!/usr/bin/python3
"""LeetCode Problem #863 --> All Nodes Distance K in Binary Tree"""
from typing import List
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def get_graph(root: TreeNode) -> None:
            if not root:
                return

            if root.left:
                graph[root.left.val].append(root.val)
                graph[root.val].append(root.left.val)
                get_graph(root.left)

            if root.right:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
                get_graph(root.right)
        get_graph(root)

        queue = deque()
        result = []
        visited = set()

        queue.append((target.val, 0))
        visited.add(target.val)
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node)
                for val, x in list(queue):
                    result.append(val)
                break

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, dist + 1))
        return result
