from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stores pairs of (start_index, height) or just indices
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # The current bar can extend backward to the popped bar's start
            stack.append((start, h))
            
        # Clean up remaining bars in the stack
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
            
        return max_area