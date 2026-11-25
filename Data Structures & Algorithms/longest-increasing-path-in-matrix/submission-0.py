class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]

            best = 1
            val = matrix[r][c]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                    length = 1 + dfs(nr, nc)
                    if length > best:
                        best = length

            dp[r][c] = best
            return best

        ans = 1
        for r in range(rows):
            for c in range(cols):
                cur = dfs(r, c)
                if cur > ans:
                    ans = cur

        return ans