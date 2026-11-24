from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0 and dp[a - coin] != INF:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return -1 if dp[amount] == INF else dp[amount]