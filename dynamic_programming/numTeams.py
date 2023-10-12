"""Leetcode Problem #1395 --> Count Number of Teams"""
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        behind = [[0, 0] for _ in range(n)]
        after = [[0, 0] for _ in range(n)]

        for i in range(n):
            greater = 0
            smaller = 0

            j = i - 1
            while j > -1:
                if rating[j] > rating[i]:
                    greater += 1

                if rating[j] < rating[i]:
                    smaller += 1

                j -= 1
            behind[i][0] = smaller
            behind[i][1] = greater

        for i in range(n):
            greater = 0
            smaller = 0

            j = i + 1
            while j < n:
                if rating[j] > rating[i]:
                    greater += 1

                if rating[j] < rating[i]:
                    smaller += 1
                j += 1

            after[i][0] = smaller
            after[i][1] = greater

        count = 0
        for i in range(n):
            behindSmaller, behindGreater = behind[i]
            afterSmaller, afterGreater = after[i]

            if behindSmaller > 0 and afterGreater > 0:
                count += behindSmaller * afterGreater

            if behindGreater > 0 and afterSmaller > 0:
                count += behindGreater * afterSmaller

        return count
