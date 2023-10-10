"""Leetcode Problem #475 --> Heaters"""
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        i, j, res = 0, 0, 0
        while i < len(houses):
            # Move the heater j to the right until we're just past house i
            while j < len(heaters) - 1 and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j += 1
            # Record the distance between house i and its closest heater
            res = max(res, abs(heaters[j] - houses[i]))
            i += 1
        return res
