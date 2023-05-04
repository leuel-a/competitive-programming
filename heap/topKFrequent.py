#!/usr/bin/python3
"""LeetCode Problem #692 --> Top K Frequent Elements"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        heap = [(-val, key) for key, val in word_count.items()]

        heapify(heap)
        result = []
        for i in range(k):
            val, key = heappop(heap)
            result.append(key)
        return result
