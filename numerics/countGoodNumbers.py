"""Leetcode Problem #1922 --> Count Good Numbers"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        MOD = pow(10, 9) + 7
        evens = n // 2 + (n % 2)
        prime = n // 2

        even_ways = pow(5, evens, MOD)
        prime_ways = pow(4, prime, MOD)

        return (even_ways * prime_ways) % MOD
