from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        inf = float("inf")
        prices = [inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp_prices = prices[:]
            updated = False

            for u, v, cost in flights:
                if prices[u] != inf and prices[u] + cost < temp_prices[v]:
                    temp_prices[v] = prices[u] + cost
                    updated = True

            prices = temp_prices
            if not updated:
                break

        return -1 if prices[dst] == inf else int(prices[dst])