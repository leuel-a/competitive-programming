from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        heap = [-num for num in nums]
        heapify(heap)

        sum_ = 0
        while len(heap) > 1:
            _ = heappop(heap)
            b = heappop(heap)

            sum_ += b

        return -sum_
