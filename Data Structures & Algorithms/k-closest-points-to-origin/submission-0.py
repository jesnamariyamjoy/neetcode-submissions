import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        max_heap = []
        
        for x, y in points:
            # We use squared distance to avoid floating-point inaccuracies
            dist = -(x**2 + y**2)
            
            # Push into the heap with the negative distance to simulate a max-heap
            heapq.heappush(max_heap, (dist, x, y))
            
            # If the heap size exceeds k, remove the farthest point (the root of the max-heap)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the points from the heap
        return [[x, y] for (dist, x, y) in max_heap]