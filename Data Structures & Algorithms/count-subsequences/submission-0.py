class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            sc = s[i - 1]
            # Iterate backward so dp[j - 1] still holds the previous row's value
            for j in range(n, 0, -1):
                if sc == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]