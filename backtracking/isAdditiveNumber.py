#!/usr/bin/python3
"""LeetCode Problem #306 --> Additive Number"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        curr = []

        def backtrack(idx: int) -> bool:
            if idx >= len(num):
                return len(curr) >= 3 

            for i in range(idx, len(num)):
                var = num[idx:i+1]
                
                if var != str(int(var)):
                    return False

                if len(curr) < 2 or curr[-2] + curr[-1] == int(var):
                    curr.append(int(var))
                    if backtrack(i+1):
                        return True
                    curr.pop()
            return False
        return backtrack(0)
