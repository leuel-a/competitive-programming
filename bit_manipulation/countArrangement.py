#!/usr/bin/python3
"""LeetCode Problem #526 --> Beautiful Arrangement"""


class Solution:
    def __init__(self) -> None:
        self.count = 0

    def countArrangement(self, n: int) -> int:
        perms, nums = [], list(range(1, n + 1))

        used = 0
        def backtrack(idx: int) -> None:
            nonlocal used
            if len(perms) == len(nums):
                self.count += 1
                return

            for i in range(n):
                if used & (1 << i) == 0:
                    used |= 1 << i
                    perms.append(nums[i])
                    if perms[idx] % (idx + 1) == 0 or (idx + 1) % perms[idx] == 0:
                        backtrack(idx + 1)
                    perms.pop()
                    used ^= 1 << i
        backtrack(0)
        return self.count
