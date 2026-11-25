class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # Ensure n <= m so the 1D DP array uses min(m, n) + 1 space
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (n + 1)
        dp[0] = True

        # Initialize first row (using 0 chars from s1, j chars from s2)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # Column 0: using i chars from s1, 0 chars from s2
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                ch = s3[i + j - 1]
                from_s1 = dp[j] and s1[i - 1] == ch
                from_s2 = dp[j - 1] and s2[j - 1] == ch
                dp[j] = from_s1 or from_s2

        return dp[n]