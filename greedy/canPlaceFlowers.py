"""Leetcode Problem #605 --> Can Place Flowers"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                if i + 1 < length:
                    if i - 1 == -1 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                    elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        return n <= 0
