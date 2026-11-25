class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i: int, j: int) -> bool:
            state = (i, j)
            if state in memo:
                return memo[state]

            if j == n:
                ans = i == m
            else:
                first_match = i < m and (p[j] == s[i] or p[j] == ".")

                if j + 1 < n and p[j + 1] == "*":
                    # Match 0 of p[j] + '*' (dfs(i, j + 2)) OR match >=1 if first_match (dfs(i + 1, j))
                    ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
                else:
                    ans = first_match and dfs(i + 1, j + 1)

            memo[state] = ans
            return ans

        return dfs(0, 0)