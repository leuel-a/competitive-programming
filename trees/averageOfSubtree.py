#!/usr/bin/python3
"""LeetCode Problem #2265 --> Count Nodes Equal to Average of Subtree"""


class Solution:
    def averageOfSubtree(self, root) -> int:
        nodes = count = 0

        def averageOfSubtreeHelper(root) -> int:
            nonlocal count, nodes

            if not root:
                return [0, 0]

            left_count, left_sum = averageOfSubtreeHelper(root.left)
            right_count, right_sum = averageOfSubtreeHelper(root.right)

            average = (left_sum + right_sum + root.val) // (left_count + right_count + 1)
            if average == root.val:
                count += 1
            return [left_count + right_count + 1, left_sum + right_sum + root.val]

        averageOfSubtreeHelper(root)
        return count
