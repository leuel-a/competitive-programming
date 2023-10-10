"""Leetcode Problem #279 --> Perfect Squares"""


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]

        if squares[-1] == n:
            return 1

        queue = {n}
        level = 0

        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square in squares:
                    if remainder == square:
                        return level
                    elif remainder < square:
                        break
                    else:
                        next_queue.add(remainder - square)
            queue = next_queue
        return level
