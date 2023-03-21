#!/usr/bin/python3
"""LeetCode Problem #617 --> Merge Two Binary Trees
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self) -> None:
        self.mergedTrees = None

    def mergedTreesHelper(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        sum = 0
        if root1 and not root2:
            sum += root1.val
            curr = TreeNode(sum)
            curr.left = self.mergedTreesHelper(root1.left, None)
            curr.right = self.mergedTreesHelper(root1.right, None)
        elif root2 and not root1:
            sum += root2.val
            curr = TreeNode(sum)
            curr.left = self.mergedTreesHelper(None, root2.left)
            curr.right = self.mergedTreesHelper(None, root2.right)
        else:
            sum += root1.val + root2.val
            curr = TreeNode(sum)
            curr.left = self.mergedTreesHelper(root1.left, root2.left)
            curr.right = self.mergedTreesHelper(root1.right, root2.right)

        return curr


    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        self.mergedTrees = self.mergedTreesHelper(root1, root2)
        # self.mergedTrees.left = self.mergedTreesHelper(root1.left, root2.left)
        # self.mergedTrees.right = self.mergedTreesHelper(root1.right, root2.right)
        return self.mergedTrees# Definition for a binary tree node.
