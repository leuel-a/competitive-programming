#!/usr/bin/python3
# LeetCode Problem #101 --> Symmetric Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetricHelper(self, root1, root2) -> bool:

        if (not root1 and root2) or (root1 and not root2):
            return False

        if root1 and root2:
            if root1.val != root2.val:
                return False
            return self.isSymmetricHelper(root1.left, root2.right) and self.isSymmetricHelper(root1.right, root2.left)
        return True


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
