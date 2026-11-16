import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate values to simulate a Max-Heap using Python's Min-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop the two heaviest stones (most negative values)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            # If they don't completely destroy each other, push the difference back
            if first != second:
                heapq.heappush(max_heap, -(first - second))
                
        # Return the remaining stone's positive weight, or 0 if empty
        return -max_heap[0] if max_heap else 0  