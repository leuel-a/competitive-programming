#!/usr/bin/python3
"""LeetCode Problem #944 --> Delete Columns to Make Sorted"""


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        for col_idx in range(len(strs[0])):
            aux = []
            for row_idx in range(len(strs)):
                aux.append(strs[row_idx][col_idx])
            if sorted(aux) != aux:
                count += 1
        return count
