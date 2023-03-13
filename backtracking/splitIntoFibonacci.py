#!/usr/bin/python3
"""LeetCode #842 --> Split Array into Fibonacci Sequence"""

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        curr = []

        def backtrack(idx: int):
            if idx >= len(num):
                return len(curr) >= 3
            
            for i in range(idx, len(num)):
                var = num[idx:i+1]

                if int(var) >= pow(2, 31):
                    return False
                if var != str(int(var)):
                    return False

                if len(curr) < 2 or curr[-1] + curr[-2] == int(var):
                    curr.append(int(var))
                    if backtrack(i+1):
                        return True
                    curr.pop()
        backtrack(0)
        return curr
