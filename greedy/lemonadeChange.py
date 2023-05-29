#!/usr/bin/python3
"""LeetCode Problem #860 --> Lemonade Change"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initial Denominations Will Be Zero
        denominations = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            # Accepting Bill From The Customer
            denominations[bill] += 1

            # How Should I Give Back The His Change, If He/She Has One?
            change = bill - 5

            if change == 0:
                continue

            if change == 5:
                if denominations[5] == 0:
                    return False
                denominations[5] -= 1
            else:
                if denominations[10] > 0 and denominations[5] > 0:
                    denominations[10] -= 1
                    denominations[5] -= 1
                elif denominations[5] >= 3:
                    denominations[5] -= 3
                else:
                    return False
        return True
