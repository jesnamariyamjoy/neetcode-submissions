import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # Min-heap of (elapsed_time, node)
        min_heap = [(0, k)]
        shortest = {}

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            # Ignore stale entries if we already recorded a shorter path to `node`
            if node in shortest:
                continue

            shortest[node] = dist

            for nxt, weight in adj[node]:
                if nxt not in shortest:
                    heapq.heappush(min_heap, (dist + weight, nxt))

        if len(shortest) != n:
            return -1

        return max(shortest.values())