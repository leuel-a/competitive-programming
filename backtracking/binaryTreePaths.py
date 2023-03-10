#!/usr/bin/python3
"""LeetCode Problem #257 --> Binary Tree Paths"""

class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        pathsToLeaf = []

        def backtrack(root, path):
            if not root:
                return

            if not root.left and not root.right:
                path.append(root.val)
                pathsToLeaf.append('->'.join(str(v) for v in path))
                path.pop()
                return

            path.append(root.val)
            backtrack(root.left, path)
            backtrack(root.right, path)
            path.pop()

        backtrack(root, [])
        return pathsToLeaf
