#!/usr/bin/python3
"""LeetCode Problem #1046 --> Last Stone Weight"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if y != x:
                y, x = -y, -x
                heapq.heappush(stones, -(y - x))
        return 0 if len(stones) == 0 else -1 * stones[0]
