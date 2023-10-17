"""Leetcode Problem #204 --> Count Primes"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        d = 2
        while d * d <= n:
            if is_prime[d]:
                j = d * d
                while j <= n:
                    is_prime[j] = False
                    j += d
            d += 1

        primes = []
        for idx, num in enumerate(is_prime):
            if num == True and idx < n:
                primes.append(idx)
        return len(primes)
