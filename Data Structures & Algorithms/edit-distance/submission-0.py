class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m

        # Ensure n <= m so the 1D array uses min(m, n) + 1 space
        if n > m:
            word1, word2 = word2, word1
            m, n = n, m

        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] = i
            c1 = word1[i - 1]

            for j in range(1, n + 1):
                temp = dp[j]  # Will become prev_diag for j + 1
                if c1 == word2[j - 1]:
                    dp[j] = prev_diag
                else:
                    # min(insert: dp[j - 1], delete: dp[j], replace: prev_diag) + 1
                    best_prev = dp[j - 1] if dp[j - 1] < dp[j] else dp[j]
                    if prev_diag < best_prev:
                        best_prev = prev_diag
                    dp[j] = 1 + best_prev
                prev_diag = temp

        return dp[n]