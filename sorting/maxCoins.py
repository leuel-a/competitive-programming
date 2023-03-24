#!/usr/bin/python3
"""LeetCode Problem #1561 --> Maximum Number of Coins You Can Get"""


class Solution:
    def quick_sort(self, arr: list[int], start: int, end: int):
        if end - start <= 0:
            return

        pivot, write = arr[start], start + 1
        for read in range(start + 1, end + 1):
            if arr[read] < pivot:
                arr[write], arr[read] = arr[read], arr[write]
                write += 1
        arr[start], arr[write - 1] = arr[write - 1], arr[start]

        self.quick_sort(arr, start, write - 2)
        self.quick_sort(arr, write, end)

    def maxCoins(self, piles: list[int]) -> int:
        _max, j = 0, 0
        _bob = {}
        self.quick_sort(piles, 0, len(piles) - 1)

        print(piles)
        for i in range(len(piles) - 2, 0, -2):
            if i not in _bob:
                _max += piles[i]
            _bob[j] = False
            j += 1

        return _max
