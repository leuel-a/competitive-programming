#!/usr/bin/python3
"""LeetCode Problem #7 --> Reverse Integer"""


class Solution:
    def reverse(self, x: int) -> int:
        aux = None

        if x < 0:
            aux = str(x)[:0:-1]
        else:
            aux = str(x)[::-1]

        aux = int(aux)
        if x < 0:
            aux *= -1
        return aux if -1 * pow(2, 31) <= aux <= pow(2, 31) - 1 else 0
