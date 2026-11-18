class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Check bounds and if the current cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current land cell as visited by sinking it ('0')
            grid[r][c] = '0'
            
            # Recursively visit all 4 neighboring directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
                    
        return islands