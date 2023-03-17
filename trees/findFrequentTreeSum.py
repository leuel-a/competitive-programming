#!/usr/bin/python3
"""LeetCode Problem #508 --> Most Frequent Subtree Sum"""


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        _sums = []

        def findTreeSum(root: Optional[TreeNode]) -> None:
            if not root:
                return 0

            left = findTreeSum(root.left)
            right = findTreeSum(root.right)
            
            _sums.append(left + right + root.val)
            return left + right + root.val

        findTreeSum(root)
        
        dict_s = Counter(_sums)
        _max = max(dict_s.values())

        res = []
        for key, val in dict_s.items():
            if val == _max:
                res.append(key)
        return res
