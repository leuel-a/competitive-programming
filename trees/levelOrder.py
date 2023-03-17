#!/usr/bin/python3
"""LeetCode Problem #102 --> Binary Tree Level Order Traversal"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_s = defaultdict(list)

        def levelOrderHelper(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return

            dict_s[level].append(root.val)
            levelOrderHelper(root.left, level + 1)
            levelOrderHelper(root.right, level + 1)

        levelOrderHelper(root, 0)
        sorted(dict_s.items())
        nodes = [val for val in dict_s.values()]
        return nodes
