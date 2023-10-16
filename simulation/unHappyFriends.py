"""Leetcode Problem #1583 --> Count Unhappy Friends"""
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Process the incoming preferences list
        processed = [[-1] * n for _ in range(n)]
        processed_pairs = {}

        for a, b in pairs:
            processed_pairs[a] = b
            processed_pairs[b] = a

        for friend, preference in enumerate(preferences):
            maxPreference = n - 1
            for person in preference:
                processed[friend][person] = maxPreference
                maxPreference -= 1

        count = 0
        for i in range(n):
            pair = processed_pairs[i]
            pair_score = processed[i][pair]

            for idx, val in enumerate(processed[i]):
                if val > pair_score:
                    its_pair = processed_pairs[idx]

                    its_pair_score = processed[idx][its_pair]
                    curr_pair = processed[idx][i]

                    if curr_pair > its_pair_score:
                        count += 1
                        break
        return count
