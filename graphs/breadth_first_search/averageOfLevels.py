#!/usr/bin/python3
"""LeetCode Problem #637 --> Average of Levels in Binary Tree"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages, queue = [], deque([root])
        while queue:
            curr_len = len(queue)

            _sum = 0
            for i in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                _sum += node.val

            averages.append(_sum / curr_len)
        return averages
