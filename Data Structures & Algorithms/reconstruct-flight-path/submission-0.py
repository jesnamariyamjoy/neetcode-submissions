from collections import defaultdict, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        route = []

        def dfs(airport: str) -> None:
            while adj[airport]:
                nxt = adj[airport].popleft()
                dfs(nxt)
            route.append(airport)

        dfs("JFK")
        return route[::-1]