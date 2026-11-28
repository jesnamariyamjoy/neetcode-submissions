class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))

        # Use row 0 and col 0 as markers for rows [1..m-1] and cols [0..n-1]
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out inner cells based on markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out first column if marked
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        # Zero out first row if it originally had a zero
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0