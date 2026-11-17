import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # The root of the min-heap is the k-th largest element
        return min_heap[0]     