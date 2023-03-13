#!/usr/bin/python3
"""LeetCode Problem #306 --> Additive Number"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        curr = []

        def backtrack(idx: int) -> bool:
            if idx >= len(num):
                return idx == len(num)

            for i in range(idx, len(num)):
                var = num[idx:i+1]
                
                if var != str(int(var)):
                    continue

                if len(curr) >= 2 and curr[-2] + curr[-1] == int(var):
                    curr.append(int(var))
                    backtrack(i+1)
                    curr.pop()

            return False
        return backtrack(0)

sol = Solution()
print(sol.isAdditiveNumber('112'))
