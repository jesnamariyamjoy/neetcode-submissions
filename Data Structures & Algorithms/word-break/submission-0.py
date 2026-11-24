from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        if not words:
            return False

        n = len(s)
        max_len = max(len(w) for w in words)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            for j in range(i - 1, start - 1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]