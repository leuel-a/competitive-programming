"""Leetcode Problem #1359 --> Count All Valid Pickup and Delivery Options"""


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [0 for _ in range(n + 1)]

        # Base Cases
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            ways = 2 * (i - 1) + 1
            dp[i] = (((ways * (ways + 1)) / 2) * dp[i - 1]) % MOD

        return int(dp[n])
