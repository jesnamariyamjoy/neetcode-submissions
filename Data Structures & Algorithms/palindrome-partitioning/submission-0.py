class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        current = []

        # Precompute palindrome table: dp[i][j] is True iff s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        def backtrack(start: int) -> None:
            if start == n:
                result.append(list(current))
                return

            for end in range(start, n):
                if dp[start][end]:
                    current.append(s[start : end + 1])
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return result 