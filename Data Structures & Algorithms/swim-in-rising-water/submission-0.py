import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (max_elevation_so_far, row, col)
        visited[0][0] = True

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (next_time, nr, nc))

        return -1