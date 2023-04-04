#!/usr/bin/python3
"""LeetCode Problem #2521 --> Distinct Prime Factors of Product of Array"""
from collections import defaultdict


class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        is_prime = [True for i in range(1001)]
        is_prime[0] = is_prime[1] = False

        d = 2
        while d * d <= 1000:
            j = d * d
            while j <= 1000:
                is_prime[j] = False
                j += d
            d += 1

        primes = []
        for i, val in enumerate(is_prime):
            if val:
                primes.append(i)

        _dict = defaultdict(set)
        for num in range(1, 1001):
            for j in primes:
                if num % j == 0:
                    _dict[num].add(j)

        distnict_prime = set()
        for num in nums:
            distnict_prime = distnict_prime.union(_dict[num])
        return len(distnict_prime)
