#!/usr/bin/python3
"""LeetCode #875 --> Koko Eating Bananas"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def calculateHourTaken(speed: int) -> int:
            count = 0
            for pile in piles:
                count += ceil(pile / speed)
            return count


        while low <= high:
            mid = low + (high - low) // 2

            if calculateHourTaken(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
