#!/usr/bin/python3
"""LeetCode Problem #2523 --> Closest Prime Numbers in Range"""


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        is_prime = [True for i in range(right + 1)]
        is_prime[0] = is_prime[1] = False

        d = 2
        while d * d <= right:
            if is_prime[d]:
                i = d * d
                while i <= right:
                    is_prime[i] = False
                    i += d
            d += 1

        primes, _min = [], float('inf')
        for i in range(left, right + 1):
            if is_prime[i] == True:
                primes.append(i)

        result = [-1, -1]
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < _min:
                _min = primes[i] - primes[i - 1]
                result[0], result[1] = primes[i - 1], primes[i]
        return result
