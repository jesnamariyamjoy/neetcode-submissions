from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(curr: int, parent: int) -> bool:
            visited.add(curr)
            for nxt in adj[curr]:
                if nxt == parent:
                    continue
                if nxt in visited or not dfs(nxt, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n