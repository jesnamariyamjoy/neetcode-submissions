class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        
        while l < r:
            # Calculate current container area
            width = r - l
            current_water = width * min(heights[l], heights[r])
            max_water = max(max_water, current_water)
            
            # Move the pointer with the smaller height inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_water