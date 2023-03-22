#!/usr/bin/python3
"""LeetCode Problem #230 --> Kth Smallest Element in a BST"""

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        inorder_traversal = []

        def traverse_tree(root) -> int:
            if not root:
                return

            traverse_tree(root.left)
            inorder_traversal.append(root.val)

            if len(inorder_traversal) == k:
                return

            traverse_tree(root.right)
        traverse_tree(root)
        return inorder_traversal[k - 1]
