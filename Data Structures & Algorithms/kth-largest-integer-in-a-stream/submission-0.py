import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Push the new value into the min-heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, evict the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the k-th largest element
        return self.min_heap[0]