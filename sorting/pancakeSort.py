#!/usr/bin/python3
"""LeetCode Problem #969 --> Pancake Sort"""


class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:

        def flip_array(end: int) -> None:
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        output = []
        for i in range(len(arr) - 1, -1, -1):
            _max = i
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[_max]:
                    _max = j
            if _max != i:
                flip_array(_max)
                flip_array(i)
                output.append(_max + 1)
                output.append(i + 1)
        return output




