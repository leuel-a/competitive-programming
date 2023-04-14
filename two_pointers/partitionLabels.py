#!/usr/bin/python3
"""LeetCode Problem #763 --> Partition Labels"""
from collections import Counter


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        seen = set()
        partition_length = []
        count_letters = Counter(s)

        i = 0
        for j, char in enumerate(s):
            seen.add(char)
            count_letters[char] -= 1

            check = list(seen)
            for elem in check:
                if count_letters[elem] == 0:
                    seen.remove(elem)

            if len(seen) == 0:
                partition_length.append(j - i + 1)
                i = j + 1
            j += 1

        return partition_length
