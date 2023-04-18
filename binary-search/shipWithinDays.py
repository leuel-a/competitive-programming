#!/usr/bin/python3
"""LeetCode #1011 --> Capacity To Ship Packages Within D Days"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        prefixSum, maximum = [], weights[0]

        prefixSum.append(0)
        for weight in weights:
            if weight > maximum:
                maximum = weight
            prefixSum.append(weight + prefixSum[-1])

        def shipWithinDaysHelper(maximumWeight: int, dayGiven: int):
            previousGone = previous = 0
            for sumWeight in prefixSum:
                if (sumWeight - previousGone) > maximumWeight:
                    dayGiven -= 1
                    previousGone = previous
                previous = sumWeight
            return dayGiven >= 1

        low, high = maximum, prefixSum[-1]
        while low <= high:
            mid = low + (high - low) // 2

            if shipWithinDaysHelper(mid, days):
                high = mid - 1
            else:
                low = mid + 1
        return low
