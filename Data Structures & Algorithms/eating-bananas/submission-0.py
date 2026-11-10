class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = left + (right - left) // 2
            
            # Calculate total hours needed at speed k
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
                
            if hours <= h:
                res = k
                right = k - 1  # Try to find a smaller valid speed
            else:
                left = k + 1   # Speed is too slow, increase k
                
        return res